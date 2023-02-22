import re, base64
from typing import List, Set
from wcapi.types.blueprints import BluePrint

string_to_base64 = lambda x: base64.b64encode(x.encode('ascii')).decode('ascii')

def build_url(path: str, obj: object):
    pass


def classify_name(name:str) -> str:
    return "".join([n.capitalize() for n in name.split('_')])

def get_args_of(pattern:str, name:str) -> str:
    pattern = pattern.replace('/wc/v3/', '').replace('/wc/v3', '')
    splited = pattern.split('/')
    args = []
    for index, part in enumerate(splited):
        if part == name:
            for after_part in splited[index+1:]:
                if re.compile(after_part).groupindex:
                    for arg, _ in re.compile(after_part).groupindex.items():
                        args.append(arg)
                else:
                    if args:
                        args = []
            break
    return args    

def make_path_of_node(pattern:str) -> List[BluePrint]:
    pattern = pattern.replace('/wc/v3/', '').replace('/wc/v3', '')
    splited = pattern.split('/')
    path = []
    for part in splited:
        if re.compile(part).groupindex: continue
        else:
            if part:
                path.append({'name': part, 'class_name': classify_name(part)})

    return path

    