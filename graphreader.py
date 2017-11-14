#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import compile
from graph import Graph

class Reader:
    pattern = compile(r'(\d+)\s+(\d+)\s+\|\s+(\d+.\d+)')

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        graph = Graph()
        with open(self.filename) as f:
            for l in f:
                if 'Graph has' in l:
                    continue
                m = self.pattern.match(l)
                if m:
                    s, t, c = m.groups()
                    graph.add_edge(int(s), int(t), float(c))
        return graph
