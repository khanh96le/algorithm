import numpy as np

class TSP:
  def __init__(self, cities, start_city, costs = []):
    self.cities = cities
    self.start_city = start_city
    self.costs = np.array(costs)
    self.mark = np.zeros(10, dtype=np.int32)
    self.mark[start_city] = 1
    pass


  def greedy_tsp(self):
    count = 1
    current_city = self.start_city
    while count < self.cities:
      for cost in self.costs[current_city]:
        if (self.mark[cost] == 0):
          pass
      count = count + 1
    pass


