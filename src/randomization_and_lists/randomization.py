import random

random_int = random.randint(1, 10)
print(f"Random int: {random_int}")

random_float = round(random.random() * 500, 2)
print(f"Random float: {random_float}")

coin = random.randint(0, 1)

if coin == 0:
    print("Heads")
else:
    print("Tails")
