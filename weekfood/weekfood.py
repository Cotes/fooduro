import random


class WeekFood:

    def __init__(self):
        self.next_dish = -1
        self.dishes = []

    def load(self, dishes):
        self.dishes = dishes

    def what_to_eat(self):
        self.next_dish += 1
        if self.next_dish >= len(self.dishes):
            self.next_dish = 0
            self.dishes = self.shuffle_dishes()
        return self.dishes[self.next_dish]

    def shuffle_dishes(self):
        if len(self.dishes) in [1, 2]:
            return self.dishes
        new_dishes = self.shuffle(list(self.dishes))
        while new_dishes == self.dishes or new_dishes[0] == self.dishes[-1]:
            new_dishes = self.shuffle(new_dishes)
        return new_dishes

    def shuffle(self, dishes):
        random.shuffle(dishes)
        return dishes
