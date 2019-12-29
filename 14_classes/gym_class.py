class Human:
    def __init__(self):
        self.energy = 0

    def eat(self, calories):
        self.energy = self.energy + calories

    def workout(self, calories):
        self.energy = self.energy - calories

gagan = Human()

print(gagan.energy)

gagan.eat(100)

print(gagan.energy)

gagan.workout(60)

print(gagan.energy)

