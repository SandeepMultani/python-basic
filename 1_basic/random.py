import random

ran1 = random.randrange(1,10)
ran2 = random.randrange(1,10)

while ran2 == ran1: #only run if both are same
    ran2 = random.randrange(1,10)



print(ran1)
print(ran2)