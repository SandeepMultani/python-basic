class Human:
    def __init__(self):
        self.energy = 0

    def eat(self, calories):
        self.energy = self.energy + calories

    def workout(self, calories):
        if calories > self.energy:
            calories = self.energy
            print("Not enough energy. Burning rest of {0} calories.".format(calories))
        
        self.energy = self.energy - calories

gagan = Human()

print(gagan.energy)

gagan.eat(100)

print(gagan.energy)

gagan.workout(60)

print(gagan.energy)

gagan.eat(10)

print(gagan.energy)

gagan.workout(110)

print(gagan.energy)

