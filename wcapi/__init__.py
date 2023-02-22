from wcapi.types import (
    WooCommerceSite,
    BluePrint,
    Node,
    getmethods
)
from wcapi.exceptions import (
    UnsupportedWooCommerceVesrion,
    FaildGETIndex,
    BuildAPIError
)
from requests_oauthlib import OAuth1Session
from urllib import parse as parse_url
from  wcapi.factory import build_tree
from typing import List
from wcapi.request import Request


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
        def factory(node_tree: dict[str, BluePrint], base: object) -> List[Node]:
            clss = []

            def build_chain(name, blueprint: BluePrint, parent = None) -> Node:
                cls = type(name, (Node, Request, ), dict({
                    '_': blueprint,
                    'parent': parent
                }))
                for key, val in blueprint.items():
                    if key[0].isupper():
                        val = build_chain(key, val, cls)
                        cls = type(name, (cls, ), dict({key: val}))

                cls = type(name, (cls, ) + tuple(getmethods(blueprint['endpoints']['methods'])), dict())

                return cls

            for name, blueprint in node_tree.items():
                clss.append(build_chain(name, blueprint, base))

            return clss
        
        self._resolve_index()
        routes = self._index.get('routes')
        
        if isinstance(routes, dict):
            tree = build_tree(routes)
            nodes = factory(tree, self)
            for node in nodes:
                setattr(self, node._['class_name'], node)
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
