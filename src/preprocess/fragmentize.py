from utils import get_node_type
from utils import is_node_list
from utils import list_dir
from utils import load_ast
from utils import pool_map

from utils.logger import print_msg
from utils.node import PORP_DICT
from utils.node import TERM_TYPE


def framentize(ast_path):
    try:
        file_name, ast = load_ast(ast_path)
    except Exception as e:
        print_msg(str(e), "WARN")
        return
    
    frag_seq = []
    make_frags(ast, frag_seq)


def main(pool, conf):
    ast_list = list_dir(conf.ast_dir)
    ast_data = pool_map(pool, fragmentize, ast_list)
    return ast_data


def make_frags(node, frag_seq):
    node_type = get_node_type(node)
    pass


if __name__ == "__Main__":
    # '../data/ast/7fe0f1bf313bbf91780e927100d557ab_aug.json' 
    fragmentize()

