from wcapi.types import (
    Node,
    GET,
    POST,
    PUT,
    PATCH,
    DELETE,
)
from wcapi.utils import make_path_of_node
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from wcapi import WooCommerceAPI


def get_method(method_name_upper:str) -> object:
    if method_name_upper == 'GET': return GET
    if method_name_upper == 'POST': return POST
    if method_name_upper == 'PUT': return PUT
    if method_name_upper == 'PATCH': return PATCH
    if method_name_upper == 'DELETE': return DELETE


def build_tree(base: 'WooCommerceAPI', routes: dict) -> ...:

    tree = {}  

    for path, details in routes.items():

        current = None
        for depth in make_path_of_node(path):
            if not current:
                current = tree

            if current.get(depth['class_name']):
                current = current.get(depth['class_name'])
            else:
                current[depth['class_name']] = depth


    print(tree['Data'])