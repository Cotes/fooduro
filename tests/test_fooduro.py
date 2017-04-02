import unittest
from fooduro.fooduro import Fooduro

class FooduroTest(unittest.TestCase):

    def test_is_working(self):
        self.assertEqual(1, 1)

    def test_when_food_is_consumed_counter_is_increased(self):
        fooduro = Fooduro()
        fooduro.consume("food")
        self.assertEqual(1, fooduro.food)