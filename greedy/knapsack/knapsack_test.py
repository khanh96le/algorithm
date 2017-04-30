import unittest
from greedy.knapsack.knapsack import Item
from greedy.knapsack.knapsack import Knapsack

class TestKnapsackAlgorithm(unittest.TestCase):

  def test_init_item(self):
    item = Item(5, 10)
    assert item.__repr__() == 'Item (5, 10)'
    item = Item(9, 10)
    assert item.__repr__() == 'Item (9, 10)'
    pass

  def test_init_knapsack(self):
    item1 = Item(4, 6)
    item2 = Item(5, 7)
    item3 = Item(12, 8)
    items = [item1, item2, item3]
    bag = Knapsack(10, items)
    assert bag.items[0].value == 6
    pass

  def test_sort_items_by_value(self):
    item1 = Item(5, 7)
    item2 = Item(4, 6)
    item3 = Item(12, 8)
    items = [item1, item2, item3]
    bag = Knapsack(10, items)
    bag.sort_value_item()
    assert bag.items[0].value >= bag.items[1].value
    assert bag.items[1].value >= bag.items[2].value
    pass

  def test_greedy1(self):
    item1 = Item(5, 7)
    item2 = Item(4, 6)
    item3 = Item(12, 8)
    items = [item1, item2, item3]
    bag = Knapsack(10, items)
    assert bag.greedy1()['value'] == 13
    assert bag.greedy1()['sum_weight'] == 9
    pass

  def test_greedy2(self):
    item1 = Item(3, 9)
    item2 = Item(8, 15)
    item3 = Item(5, 2)
    items = [item1, item2, item3]
    bag = Knapsack(10, items)
    assert bag.greedy1()['value'] == 15
    assert bag.greedy2()['value'] == 11
    assert bag.greedy3()['value'] == 11


  def test_greedy3(self):
    item1 = Item(5, 20)
    item2 = Item(3, 9)
    item3 = Item(5, 10)
    item4 = Item(2, 2)
    item5 = Item(1, 1)
    items = [item1, item2, item3, item4, item5]
    bag = Knapsack(10, items)
    assert bag.greedy1()['value'] == 30
    assert bag.greedy2()['value'] == 12
    assert bag.greedy3()['value'] == 31








