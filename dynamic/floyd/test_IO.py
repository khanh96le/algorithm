from unittest import TestCase
from dynamic.floyd.floyd import IO


class TestIO(TestCase):
  def test_read_file_input(self):
    io = IO()
    graph1 = io.read_file_input('data/data1')
    assert len(graph1.nodes) == 4
    self.fail()
