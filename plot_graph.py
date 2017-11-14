#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from os import path
from graphreader import Reader

def parse_args():
    arg_parser = ArgumentParser(description='TODO')
    arg_parser.add_argument("filename")
    return arg_parser.parse_args()

out_format = 'svg'

def get_out_filename(filename):
    base, _ = path.splitext(filename)
    return base + '.' + out_format

if __name__ == "__main__":
    args = parse_args()
    graph = Reader(args.filename).read()
    graph.write(get_out_filename(args.filename))
