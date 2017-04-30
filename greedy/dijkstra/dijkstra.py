from IPython.core.display import Math
from collections import defaultdict
import pandas as pd

INF = 100000

class Graph:
  def __init__(self):
    """
    A graph contains: Node, Edge and Distance between nodes
    """
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_nodes(self, value):
    self.nodes.add(value)

  def add_edges(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance

  def dijkstra(self, initial):
    graph = self
    d = {}
    free = {}
    trace = {}
    for vertice in graph.nodes:
      d[vertice] = INF
      free[vertice] = False
    d[initial] = 0

    while True:
      min = INF
      select_node = 0
      for node in graph.nodes:
        if (free[node] == False and d[node] < min):
          min = d[node]
          select_node = node
      if (select_node == 0):
        break

      free[select_node] = True

      for node in graph.nodes:
        try:
          if(free[node] == False and d[node] > d[select_node] + graph.distances[(select_node, node)]):
            d[node] = d[select_node] + graph.distances[(select_node, node)]
            trace[node] = select_node
        except:
          pass

      print select_node
    return {'result': d, 'trace': trace}

class IO:
  def read_file_input(self, file):
    try:
      with open(file) as f:
        lines = f.readlines()
    except (Exception):
      print Exception

    number_nodes = int(lines[0].split(' ')[0])
    graph = Graph()
    for node in range(1, number_nodes + 1):
      graph.add_nodes(node)
    for line in lines[1:number_nodes + 1]:
      from_node, to_node, distance = tuple(line.split(' '))
      graph.add_edges(int(from_node), int(to_node), int(distance))
    return graph

