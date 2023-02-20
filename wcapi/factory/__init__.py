from wcapi.types import BluePrint
from wcapi.utils import make_path_of_node, get_args_of
from typing import Set



def add_attrs(path:str, name:str, current:BluePrint, details: dict) -> None:
    args = get_args_of(path, name)
    if args:
        init_kwargs: Set[str] = current.get('init_kwargs')
        if init_kwargs:
            init_kwargs.union(set(args))
        else:
            init_kwargs = set(args)
        current['init_kwargs'] = init_kwargs
    
    if not current.get('endpoints'):
        current.update({'endpoints': {
            'methods': set(),
            'args': []
        }})

    current['endpoints']['methods'] = current['endpoints']['methods'].union(set(details['methods']))
    current['endpoints'].update({'args': current['endpoints']['args'] + details['endpoints']})

def build_tree(routes: dict) -> ...:

    tree = {}

    for path, details in routes.items():
        current = None
        for depth in make_path_of_node(path):
            if not current:
                current = tree

            if current.get(depth['class_name']):
                current = current.get(depth['class_name'])
                add_attrs(path, depth['name'], current, details)
            else:
                current[depth['class_name']] = depth
                add_attrs(path, depth['name'], current[depth['class_name']], details)
                
    return tree