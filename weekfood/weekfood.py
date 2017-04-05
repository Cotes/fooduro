import random


class WeekFood:

    def __init__(self):
        self.next_dish = -1
        self.dishes = []

    def load(self, dishes):
        self.dishes = dishes

    def whats_to_eat(self):
        self.next_dish += 1
        if self.next_dish >= len(self.dishes):
            self.next_dish = 0
            old_dishes = list(self.dishes)
            random.shuffle(self.dishes)
            while old_dishes == self.dishes:
                random.shuffle(self.dishes)
        return self.dishes[self.next_dish]
