from wcapi.exceptions import (
    HTTPMethodNotDefiend
)
from typing import List

class GET:
    @classmethod
    def GET(cls, **kwargs) -> ...:
        cls.handle_http_method('GET', **kwargs)

class POST:
    @classmethod
    def POST(cls, **kwargs) -> ...:
        cls.handle_http_method('POST', **kwargs)

class PUT:
    @classmethod
    def PUT(cls, **kwargs) -> ...:
        cls.handle_http_method('PUT', **kwargs)

class PATCH:
    @classmethod
    def PATCH(cls, **kwargs) -> ...:
        cls.handle_http_method('PATCH', **kwargs)

class DELETE:
    @classmethod
    def DELETE(cls, **kwargs) -> ...:
        cls.handle_http_method('DELETE', **kwargs)

def getmethod(method:str) -> object:
    if method == 'GET': return GET
    if method == 'POST': return POST
    if method == 'PUT': return PUT
    if method == 'PATCH': return PATCH
    if method == 'DELETE': return DELETE
    raise HTTPMethodNotDefiend(f'Method {method} not implemented')

def getmethods(methods:List[str]) -> List[object]:
    methods_ = []
    for method in methods:
        mtd = getmethod(method)
        if mtd:
            methods_.append(mtd)
    return methods_
