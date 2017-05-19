from unittest import TestCase
from utils.graph_generator import GraphGenerator
from utils.graph import Graph

class TestGraphGenerator(TestCase):
    def test_generateGraphFromFile(self):
        file_name = "../data/data1"
        graph = Graph()
        graphGenerator = GraphGenerator()
        graph = graphGenerator.generateGraphFromFile(file_name)
        assert graph.edges[6].__len__() == 3
