from typing import Any


class Request:

    @classmethod
    def handle_http_method(cls, method:str, **kwargs) -> Any:
        print(cls._.get('path'))