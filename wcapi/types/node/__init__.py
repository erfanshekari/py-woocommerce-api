from typing import Any, List, Tuple, Union
from wcapi.types.blueprints import BluePrint



class Node:

    _: BluePrint
    parent: Any
    init_inputs: Union[Tuple[List[Any], dict[str, Any]], None]

    def __init__(self, *args, **kwargs) -> None:
        self.init_inputs = (args, kwargs)
    