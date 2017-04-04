class Fooduro:

    def load(self, *dishes):
        self.dishes = list(dishes)

    def whats_to_eat(self):
        return self.dishes[0]
