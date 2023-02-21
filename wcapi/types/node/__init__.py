from typing import Any, Union
from wcapi.types.blueprints import BluePrint
from wcapi.exceptions import (
    NotEnoughKwargs
)

class Node:

    _: BluePrint
    parent: Any

    def __init__(self, *args, **kwargs) -> None:
        pass
        