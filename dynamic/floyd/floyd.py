from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_nodes(self, value):
    self.nodes.add(value)

  def add_edges(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance

class Floyd:
  def __init__(self):
    pass


class IO:
  def read_file_input(self,file):
    try:
      with open(file) as f:
        lines = f.readlines()
    except Exception, e:
      print e.message

    number_nodes = int(lines[0].split(' ')[0])
    graph = Graph()
    for node in range(1, number_nodes + 1):
      graph.add_nodes(node)
    for line in lines[1:number_nodes + 1]:
      from_node, to_node, distance = tuple(line.split(' '))
      graph.add_edges(int(from_node), int(to_node), int(distance))
    return graph


