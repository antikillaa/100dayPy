with open("./Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

for name in names:
    new_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{new_name}", "x") as file:
        new_letter = letter.replace("[name]", new_name)
        file.write(new_letter)
