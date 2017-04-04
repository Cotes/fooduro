import unittest
from weekfood.weekfood import WeekFood


class WeekFoodTest(unittest.TestCase):

    def setUp(self):
        self.weekFood = WeekFood()
        self.dishes = ["aDish", "anotherDish"]
        self.weekFood.load(list(self.dishes))

    def test_when_initialization_load_food(self):
        self.assertEqual(["aDish", "anotherDish"], self.weekFood.dishes)

    def test_when_we_ask_for_a_dish_should_serve_one(self):
        self.assertIn(self.weekFood.whats_to_eat(), ["aDish"])

    def test_asking_for_two_dishes_should_not_repeat_them_if_possible(self):
        first_dish = self.weekFood.whats_to_eat()
        self.assertIn(first_dish, self.dishes)
        self.dishes.remove(first_dish)
        self.assertIn(self.weekFood.whats_to_eat(), self.dishes)

    def test_asking_for_three_dishes_and_its_has_only_2_available(self):
        first_dish = self.weekFood.whats_to_eat()
        second_dish = self.weekFood.whats_to_eat()
        third_dish = self.weekFood.whats_to_eat()
        self.assertNotEqual(first_dish, second_dish)
        self.assertIn(third_dish, self.dishes)