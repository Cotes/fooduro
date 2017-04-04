import unittest
from fooduro.fooduro import Fooduro


class FooduroTest(unittest.TestCase):

    def setUp(self):
        self.fooduro = Fooduro()

    def test_when_initialization_load_food(self):
        self.fooduro.load("dish", "another")
        self.assertEqual(["dish", "another"], self.fooduro.dishes)
