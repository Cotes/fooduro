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
        return self.dishes[self.next_dish]
