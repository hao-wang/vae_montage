import argparse
import os
import sys
import torch

from utils.config import Config
from utils.logger import print_msg
from utils import make_dir


def exec_preprocess(conf):
    from preprocess.preprocess import Preprocessor
    preprocessor = Preprocessor(conf)
    preprocessor.preprocess()


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--opt", required=True, 
            choices=['preprocess', 'train', 'fuzz'])
    arg_parser.add_argument("--conf", required=True)
    return arg_parser.parse_args(sys.argv[1:])


def main(argv):
    sys.setrecursionlimit(1000)
    args = get_args()
    config_path = args.config
    conf = Config(config_path)

    if args.opt == "preprocess":
        exec_preprocess(conf)
    else:
        print("not implemented yet.")


if __name__ == "__main__":
    main()
