import unittest
from fooduro.fooduro import Fooduro


class FooduroTest(unittest.TestCase):

    def setUp(self):
        self.fooduro = Fooduro()

    def test_when_initialization_load_food(self):
        self.fooduro.load("aDish", "anotherDish")
        self.assertEqual(["aDish", "anotherDish"], self.fooduro.dishes)

    def test_when_we_ask_for_a_dish_should_serve_one(self):
        self.fooduro.load("aDish")
        self.assertIn(self.fooduro.whats_to_eat(), ["aDish"])
