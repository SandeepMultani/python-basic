class Car:
    def __init__(self):
        self.speed = 0
        self.tax = 0

    def apply_accelerate(self, force):
        self.speed += (1.5 * force)
        if isinstance(self, ElectricCar):
            self.discharge_battery(0.5 * force)
        else:
             self.burn_fuel(0.9 * force)

    def apply_break(self, force):
        self.speed -= (3.5 * force)

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        self.battery = 0

    def discharge_battery(self, amp):
        self.battery -= amp

    def charge_battery(self, amp):
        self.battery += amp

class ICECar(Car):
    def __init__(self):
        super().__init__()
        self.fuel = 0

    def burn_fuel(self, val):
        self.fuel -= val
        self.add_env_tax(val)

    def fill_fuel(self, val):
        self.fuel += val

class Petrol(ICECar):
    def __init__(self):
        super().__init__()

    def add_env_tax(self, val):
        self.tax += (val * 0.01)

class Diesel(ICECar):
    def __init__(self):
        super().__init__()

    def add_env_tax(self, val):
        self.tax += (val * 0.008)


print("E Car")
electricCar1 = ElectricCar()

print(electricCar1.battery)
print(electricCar1.speed)

electricCar1.charge_battery(10)
print(electricCar1.battery)

electricCar1.apply_accelerate(1)
print(electricCar1.speed)
print(electricCar1.battery)
print(electricCar1.tax)


print("P Car")

petrolCar1 = Petrol()

print(petrolCar1.fuel)
print(petrolCar1.speed)

petrolCar1.fill_fuel(10)
print(petrolCar1.fuel)

petrolCar1.apply_accelerate(1)
print(petrolCar1.speed)
print(petrolCar1.fuel)
print(petrolCar1.tax)


print("D Car")

dieselCar1 = Diesel()

print(dieselCar1.fuel)
print(dieselCar1.speed)

dieselCar1.fill_fuel(10)
print(dieselCar1.fuel)

dieselCar1.apply_accelerate(1)
print(dieselCar1.speed)
print(dieselCar1.fuel)
print(dieselCar1.tax)

