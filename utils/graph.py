from collections import defaultdict

class Graph:
    def __init__(self):
        """
        A graph contains: Node, Edge and Distance between nodes
        """
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        """
        Add node to graph
        Value of node has to be unique
        :param value:
        """
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, value):
        """
        Add a edge to graph and the distance between 2 nodes of the edge
        :param from_node:
        :param to_node:
        :param value:
        """
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = value
