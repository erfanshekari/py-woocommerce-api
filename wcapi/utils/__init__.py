import re, base64
from typing import List
from wcapi.types.blueprints import NodeMeta

string_to_base64 = lambda x: base64.b64encode(x.encode('ascii')).decode('ascii')

def classify_name(name:str) -> str:
    return "".join([n.capitalize() for n in name.split('_')])

def build_tree_path(pattern:str) -> str:
    pattern = pattern.replace('/wc/v3/', '').replace('/wc/v3', '')
    splited = pattern.split('/')
    tree_path = ""
    for part in splited:
        if re.compile(part).groupindex: continue
        tree_path += f'/{classify_name(part)}'
    return tree_path


def get_args(pattern:str) -> str:
    pattern = pattern.replace('/wc/v3/', '').replace('/wc/v3', '')
    splited = pattern.split('/')
    args = []
    for part in splited:
        if re.compile(part).groupindex:
            for arg, _ in re.compile(part).groupindex.items():
                args.append(arg)
        else:
            if args:
                args = []

    return args
        

def make_path_of_node(pattern:str) -> List[NodeMeta]:
    pattern = pattern.replace('/wc/v3/', '').replace('/wc/v3', '')
    splited = pattern.split('/')
    path = []
    for part in splited:
        if re.compile(part).groupindex: continue
        else:
            if part:
                path.append({'name': part, 'class_name': classify_name(part)})

    return path

        
def get_class_name(tree_path:str) -> str:
    return tree_path.split('/')[-1]