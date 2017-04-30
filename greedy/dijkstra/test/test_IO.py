from unittest import TestCase

from greedy.dijkstra.dijkstra import IO


class TestIO(TestCase):
  def test_read_file_input1(self):
    io = IO()
    graph1 = io.read_file_input('../data/data1')
    assert len(graph1.nodes) == 4
    assert graph1.dijkstra(1)['result'][4] == 5

    graph2 = io.read_file_input('../data/data2')
    assert len(graph2.nodes) == 5
    assert graph2.dijkstra(1)['result'][5] == 8
