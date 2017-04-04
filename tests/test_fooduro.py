import unittest
from weekfood.weekfood import WeekFood


class FooduroTest(unittest.TestCase):

    def setUp(self):
        self.weekFood = WeekFood()

    def test_when_initialization_load_food(self):
        self.weekFood.load("aDish", "anotherDish")
        self.assertEqual(["aDish", "anotherDish"], self.weekFood.dishes)

    def test_when_we_ask_for_a_dish_should_serve_one(self):
        self.weekFood.load("aDish")
        self.assertIn(self.weekFood.whats_to_eat(), ["aDish"])
