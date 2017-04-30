from unittest import TestCase
from greedy.dijkstra.dijkstra import Graph


class TestGraph(TestCase):
  def test_indirect_graph(self):
    graph = Graph()
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_nodes(3)
    graph.add_nodes(4)
    graph.add_edges(1, 2, 1)
    graph.add_edges(1, 3, 4)
    graph.add_edges(1, 4, 3)
    graph.add_edges(2, 3, 2)
    graph.add_edges(3, 4, 1)
    initial = 1
    result = graph.dijkstra(initial)
    for vertice in graph.nodes:
      print "distance from {0} to {1} is {2}".format(initial, vertice, result['result'][vertice])

    assert result['result'][3] == 3

  def test_direct_graph(self):
    graph = Graph()
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_nodes(3)
    graph.add_nodes(4)
    graph.add_edges(1, 2, 1)
    graph.add_edges(1, 3, 4)
    graph.add_edges(3, 4, 1)
    graph.add_edges(4, 1, 1)
    initial = 1
    result = graph.dijkstra(initial)
    assert result['result'][4] == 5


