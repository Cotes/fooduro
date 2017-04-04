import unittest
from fooduro.fooduro import Fooduro


class FooduroTest(unittest.TestCase):

    def setUp(self):
        self.weekFood = Fooduro()

    def test_when_initialization_load_food(self):
        self.weekFood.load("aDish", "anotherDish")
        self.assertEqual(["aDish", "anotherDish"], self.weekFood.dishes)

    def test_when_we_ask_for_a_dish_should_serve_one(self):
        self.weekFood.load("aDish")
        self.assertIn(self.weekFood.whats_to_eat(), ["aDish"])
