# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    for i in range(3):
        print("Statement")


greet()


def greet_name(name, location):
    print(f"Hello {name}\nWhat is weather in {location}?")


greet_name(input("What is your name?"), input("Where are you living?"))
