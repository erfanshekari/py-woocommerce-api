from typing import TypedDict, List


class BluePrint(TypedDict):
    endpoint: str
    init_kwargs: List[str]


class NodeMeta(TypedDict):
    class_name:str
    name:str