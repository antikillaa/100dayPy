array = [1, 2, 3, 4, 3, 2, 1]

uniq_number = 0

for number in array:
    if array.count(number) == 1:
        uniq_number = number

print(uniq_number)