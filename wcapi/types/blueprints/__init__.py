from typing import TypedDict, Set, Union, Any, List

class Endpoints(TypedDict):
    methods: Set[str]
    args: List[dict[str, Any]]

class BluePrint(TypedDict):
    class_name:str
    name:str
    init_kwargs: Union[Set[str], None]
    methods: Set[str]
    endpoints: Endpoints