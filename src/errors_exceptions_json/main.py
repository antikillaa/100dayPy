# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"Key is not {error_message} exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is my error message")


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height should be not over 3 meters")

bmi = weight / height ** 2
print(bmi)