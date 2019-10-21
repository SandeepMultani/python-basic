orange, red, blue = "Orange", "Red", "Blue"

print(orange)
print(red)
print(blue)

salary, bills, food, car = 100, 47, 20, 30

savings = salary - (bills + food + car)

output_msg = "My salary is ${} but I can only save ${} a month."
print(output_msg.format(salary, savings))

print("I spend $" + str(car) + " on my car.")

print(("My bill are ${} and I spend ${} on food.").format(bills, food))
