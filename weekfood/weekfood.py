class WeekFood:

    def __init__(self):
        self.calls = -1

    def load(self, dishes):
        self.dishes = dishes

    def whats_to_eat(self):
        self.calls += 1
        return self.dishes[self.calls]
