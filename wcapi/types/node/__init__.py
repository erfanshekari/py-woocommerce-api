from typing import Any, Union
from wcapi.types.blueprints import BluePrint
from wcapi.exceptions import (
    NotEnoughKwargs
)

class Node:

    _: BluePrint
    main: Any
    parent: Any
    name: str

    def __init__(self, *args, **kwargs) -> None:
        pass
        