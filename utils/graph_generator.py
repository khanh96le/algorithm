from conda._vendor.toolz.functoolz import excepts

from utils.graph import Graph

class GraphGenerator:
    def __init__(self):
        self.graph = Graph()

    def generateGraphFromFile(self, filename):
        """
        Read data in a file and create a new graph
        :param filename:
        :return: a graph
        """
        try:
            with open(filename) as f:
                data = f.readlines()
        except Exception, e:
            print e.message
            raise ValueError(e.message)

        try:
            # Add nodes to graph
            nodes = int(data[0])
            for node in range(1, nodes+1):
                self.graph.add_node(node)
            # Add edges to graph
            total_edges = data.__len__() - 1
            i = 1
            while i <= total_edges:
                edge = data[i].split(" ")
                edge = map(lambda x: int(x), edge)
                self.graph.add_edge(edge[0], edge[1], edge[2])
                i = i + 1
                pass
        except Exception, e:
            print e.message
            raise ValueError(e.message)
        return self.graph
