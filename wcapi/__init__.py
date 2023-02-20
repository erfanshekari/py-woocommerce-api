import pprint
from wcapi.types import (
    WooCommerceSite
)
from wcapi.exceptions import (
    UnsupportedWooCommerceVesrion,
    FaildGETIndex,
    BuildAPIError
)
from requests_oauthlib import OAuth1Session
from urllib import parse as parse_url
from wcapi.factory import build_tree


class WooCommerceAPI:

    site: WooCommerceSite
    session: OAuth1Session
    _index: dict

    def __init__(self, url: str, consumer_key:str, consumer_secret:str) -> None:
        self._index = None
        assert url and consumer_key and consumer_key
        self.site = {
            'url': parse_url.urlparse(url),
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret
        }
        
        self.session = OAuth1Session(
            self.site['consumer_key'],
            client_secret=self.site['consumer_secret']
        )

        self._build()


    def _build(self) -> None:
        self._resolve_index()

        routes = self._index.get('routes')
        
        if isinstance(routes, dict):
            tree = build_tree(routes)
            pprint.pprint(tree)
        else:
            raise BuildAPIError("No routes in _index")


    def _build_url(self, path:str) -> str:
        base_url = self.site['url'].geturl()
        if path and path[0] == '/':
            path = path[1:]
        return f'{base_url}/wp-json/{path}'
    
    def _resolve_index(self) -> None:
        url = self._build_url('/wc/v3')
        response = self.session.get(url, timeout=5)
        if response.status_code == 200:
            response_json = response.json()
            if isinstance(response_json, dict):
                self._index = response_json
            if not self._index:
                raise UnsupportedWooCommerceVesrion("WooCommerce Version Not Supported!")
        else:
            raise FaildGETIndex(f'Faild GET {url}')
