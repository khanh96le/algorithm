from unittest import TestCase

from greedy.travelling_salesman.tsp import TSP


class TestTSP(TestCase):
  def test_fuc(self):
    cost = [
      [0, 1, 2, 7, 5],
      [1, 0, 4, 4, 3],
      [2, 4, 0, 1, 2],
      [7, 4, 1, 0, 3],
      [5, 3, 2, 3, 0]
    ]
    tsp = TSP(cities=5, start_city=0, costs=cost)
    tsp.greedy_tsp()
    pass


