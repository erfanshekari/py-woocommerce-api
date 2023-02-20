

class Method:
    def _handle_method(method:str, *args, **kwargs) -> ...:...

class GET(Method):
    def GET(*args, **kwargs) -> ...:
        GET()._handle_method('GET', *args, **kwargs)

class POST(Method):
    def POST(*args, **kwargs) -> ...:
        POST()._handle_method('POST', *args, **kwargs)

class PUT(Method):
    def PUT(*args, **kwargs) -> ...:
        PUT()._handle_method('PUT', *args, **kwargs)

class PATCH(Method):
    def PATCH(*args, **kwargs) -> ...:
        PATCH()._handle_method('PATCH', *args, **kwargs)

class DELETE(Method):
    def DELETE(*args, **kwargs) -> ...:
        DELETE()._handle_method('DELETE', *args, **kwargs)