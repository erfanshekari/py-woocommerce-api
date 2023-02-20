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
    path_params: dict
    orphan_args: Union[object, None]

    def __init__(self, *args, **kwargs) -> None:
        init_kwargs = self._.get('init_kwargs')
        if init_kwargs:
            for key in init_kwargs:
                value = kwargs.get(key)
                if value:
                    self.path_params[key] = value
                else:
                    raise NotEnoughKwargs(f'You Must Provide {str(init_kwargs)} As Named Arguments')
        else:
            if args:
                self.orphan_args = args