import unittest
from fooduro.fooduro import Fooduro


class FooduroTest(unittest.TestCase):

    def setUp(self):
        self.fooduro = Fooduro()

    def test_when_initialization_load_food(self):
        self.fooduro.load("dish", "another")
        self.assertEqual(["dish", "another"], self.fooduro.dishes)

    def test_when_food_is_consumed_counter_is_increased(self):
        self.fooduro.consume("food")
        self.assertEqual(1, self.fooduro.food)
