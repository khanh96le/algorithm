from unittest import TestCase

from dynamic.fibonacci.fibonacci import Fibonacii


class TestFibonacii(TestCase):
  def test_fibonacii(self):
    fibo = Fibonacii()
    fibo.fibonacii()
