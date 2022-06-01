def strip_line(raw):
    return [int(l.strip('\n')) for l in raw]


with open("file1.txt", mode="r") as file:
    list_1_raw = file.readlines()

with open("file2.txt", mode="r") as file:
    list_2_raw = file.readlines()

final_list = [int(l) for l in list_1_raw if l in list_2_raw]

# Write your code above 👆

print(final_list)
