import unittest
from unittest.mock import Mock
from weekfood.weekfood import WeekFood


class WeekFoodTest(unittest.TestCase):

    def setUp(self):
        self.weekFood = WeekFood()

    def load_dishes(self, amount):
        self.dishes = ["aDish", "anotherDish", "moreDish"]
        self.weekFood.load(list(self.dishes[:amount]))

    def test_when_initialization_load_food(self):
        self.load_dishes(2)
        self.assertEqual(self.dishes[:2], self.weekFood.dishes)

    def test_when_we_ask_for_a_dish_should_serve_one(self):
        self.load_dishes(1)
        self.assertIn(self.weekFood.what_to_eat(), ["aDish"])

    def test_asking_for_two_dishes_should_not_repeat_them_if_possible(self):
        self.load_dishes(2)
        first_dish = self.weekFood.what_to_eat()
        self.assertIn(first_dish, self.dishes)
        self.dishes.remove(first_dish)
        self.assertIn(self.weekFood.what_to_eat(), self.dishes)

    def test_asking_for_three_dishes_and_it_has_only_2_available(self):
        self.load_dishes(2)
        first_dish = self.weekFood.what_to_eat()
        second_dish = self.weekFood.what_to_eat()
        third_dish = self.weekFood.what_to_eat()
        self.assertNotEqual(first_dish, second_dish)
        self.assertIn(third_dish, self.dishes)

    def test_avoid_cycles(self):
        num_dishes = 3
        self.load_dishes(num_dishes)
        first_cycle = self.get_dishes_for_cycle(num_dishes)
        second_cycle = self.get_dishes_for_cycle(num_dishes)
        self.assertNotEqual(first_cycle, second_cycle)

    def test_when_there_is_only_one_dish_should_always_return_it(self):
        self.load_dishes(1)
        self.assertEqual(self.weekFood.what_to_eat(), self.weekFood.what_to_eat())

    def test_avoid_repetitions_over_cycles(self):
        num_dishes = 2
        self.load_dishes(num_dishes)
        first_cycle = self.get_dishes_for_cycle(num_dishes)
        second_cycle = self.get_dishes_for_cycle(num_dishes)
        self.assertNotEqual(first_cycle[1], second_cycle[0])

    def test_avoid_repetitions_with_more_than_two_dishes(self):
        num_dishes = 3
        self.load_dishes(num_dishes)
        first_cycle = self.get_dishes_for_cycle(num_dishes)
        self.weekFood.shuffle = Mock()
        self.weekFood.shuffle.side_effect = [["moreDish", "aDish", "anotherDish"], ["anotherDish", "moreDish", "aDish"]]
        second_cycle = self.get_dishes_for_cycle(num_dishes)
        self.assertNotEqual(first_cycle[2], second_cycle[0])

    def get_dishes_for_cycle(self, num_dishes):
        second_cycle = []
        for _ in range(num_dishes):
            second_cycle.append(self.weekFood.what_to_eat())
        return second_cycle
