value = int(input("Input bill value\n"))
number_person = int(input("How many persons?\n"))
tips = int(input("How many tips? 12, 15 or 20%?\n"))

to_pay = (value + (value * tips / 100)) / number_person

print(round(to_pay, 2))
