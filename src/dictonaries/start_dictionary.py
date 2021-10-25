program_dictionary = {
    "Bug": "An error in a program",
    "Function": "A peace of code",

}

print(program_dictionary["Bug"])

program_dictionary["Loop"] = "The action of doing something"

print(program_dictionary)

for k, v in program_dictionary.items():
    print(k)
    print(v)
