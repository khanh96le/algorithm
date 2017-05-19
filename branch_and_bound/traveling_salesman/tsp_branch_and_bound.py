from utils.graph_generator import GraphGenerator

class Tsp:
    # Const number
    INFINITY = 1000000

    def __init__(self):
        pass

    def setGraph(self, graph):
        self.graph = graph
        # mark is a list to check if a node is visited or not
        # if 1 -> node has been visited
        # if 0 -> node hasn't been visited
        # from the beginning, there are no nodes are visited
        self.mark = [0] * self.graph.nodes.__len__()
        # min distance to create a min threshold
        self.min_distance = min(self.graph.distances.items())[1]
        # from the beginning, the optimize result should be infinity
        self.optimize_result = self.INFINITY
        # because the saleman starts from node 1, so 1 should exist in the scenarios
        self.result = [1]


    def travelingSaleMan(self, node):
        """
        Travel city i and find the best way to go
        :param i:
        :return:
        """
        for i in range(2, self.graph.nodes.__len__() + 1):
            if not self.mark[i]:
                self.result
                pass

        pass

if __name__ == "__main__":
    graph = GraphGenerator().generateGraphFromFile("../../data/data1")
    tsp = Tsp()
    # init graph
    tsp.setGraph(graph)
    # Start from first city
    tsp.travelingSaleMan(1)


