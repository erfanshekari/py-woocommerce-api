from typing import TypedDict, Set, Union, Any, List

class Endpoint(TypedDict):
    methods: List[str]
    args: dict[str, Any]

class Endpoints(TypedDict):
    methods: Set[str]
    endpoints: List[Endpoint]

class BluePrint(TypedDict):
    class_name:str
    name:str
    path: Union[str, None]
    init_kwargs: Union[Set[str], None]
    endpoints: Endpoints