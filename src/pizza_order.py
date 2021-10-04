from numpy.core.defchararray import lower

print("Welcome to Python Pizza Deliveries!\n")
size = lower(input("What size pizza do you want? S, M, or L \n"))
add_pepperoni = lower(input("Do you want pepperoni? Y or N \n"))
extra_cheese = lower(input("Do you want extra cheese? Y or N \n"))

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if add_pepperoni == "y" and size == "s":
    bill += 2
elif add_pepperoni == "y" and size == "m":
    bill += 3
elif add_pepperoni == "y" and size == "l":
    bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")
