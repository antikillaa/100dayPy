# 🚨 Don't change the code below 👇
from numpy.core.defchararray import lower, count

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1 = lower(name1)
name2 = lower(name2)

t = count(name1, "t") + count(name2, "t")
r = count(name1, "r") + count(name2, "r")
u = count(name1, "u") + count(name2, "u")
e1 = count(name1, "e") + count(name2, "e")

l = count(name1, "l") + count(name2, "l")
o = count(name1, "o") + count(name2, "o")
v = count(name1, "v") + count(name2, "v")
e2 = count(name1, "e") + count(name2, "e")

first_letter = str(t + r + u + e1)
second_letter = str(l + o + v + e2)

final_score = int(first_letter + second_letter)

if final_score < 10 or final_score > 90:
    print(f"Your score is **{final_score}**, you go together like coke and mentos.")
elif 40 < final_score < 50:
    print(f"Your score is **{final_score}**, you are alright together.")
else:
    print(f"Your score is **{final_score}**.")


