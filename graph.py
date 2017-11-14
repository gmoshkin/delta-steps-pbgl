#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from pydot import Dot, Node, Edge
from os import path

class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_node(self, n):
        self.nodes.add(n)

    def add_edge(self, s, t, c):
        self.add_node(s)
        self.add_node(t)
        self.edges.add((s, t, c))

    def dump_dotty(self, filename, format):
        graph = Dot(graph_type='digraph')
        dot_nodes = {}
        for n in self.nodes:
            _n = Node(n, style='filled', fillcolor='white')
            graph.add_node(_n)
            dot_nodes[n] = _n
        for s, t, c in self.edges:
            if s in dot_nodes and t in dot_nodes:
                graph.add_edge(Edge(dot_nodes[s], dot_nodes[t], label=c))
        graph.write(filename, format=format)

    def dump_text(self, filename):
        with open(filename, 'w') as of:
            for s, t, c in self.edges:
                print(s, t, '|', c, file=of)

    def write(self, filename):
        ext = path.splitext(filename)[1]
        if ext == '.svg':
            self.dump_dotty(filename, format='svg')
        elif ext == '.txt':
            self.dump_text(filename)
