
class Item:
  def __init__(self, weight, value):
    self.weight = weight
    self.value = value

  def __repr__(self):
    return "Item ({}, {})".format(self.weight, self.value)

class Knapsack:
  def __init__(self, capacity, items = []):
    self.capacity = capacity
    self.items = items

  def greedy1(self):
    items = sorted(self.items, key = lambda item: item.value, reverse=True)
    sum = 0
    value = 0
    for item in items:
      if sum + item.weight <= self.capacity:
        sum = sum + item.weight
        value = value + item.value
    return {"sum_weight":sum, "value":value}

  def greedy2(self):
    items = sorted(self.items, key = lambda item: item.weight, reverse=False)
    sum = 0
    value = 0
    for item in items:
      if sum + item.weight <= self.capacity:
        sum = sum + item.weight
        value = value + item.value
    return {"sum_weight":sum, "value":value}

  def greedy3(self):
    items = sorted(self.items, key = lambda item: item.value / item.weight , reverse=True)
    sum = 0
    value = 0
    for item in items:
      if sum + item.weight <= self.capacity:
        sum = sum + item.weight
        value = value + item.value
    return {"sum_weight":sum, "value":value}







