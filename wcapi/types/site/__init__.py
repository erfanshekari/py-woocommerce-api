from typing import TypedDict
from urllib.parse import ParseResult


class WooCommerceSite(TypedDict):
    url: ParseResult
    consumer_key: str
    consumer_secret: str