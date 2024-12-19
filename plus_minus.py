arr = [1, 2, 3, -1, -2, -3, 0, 0]

positive_integer = 0
negative_integer = 0
zero_integer = 0

arr_size = len(arr)

for i in range(0, arr_size):
    number = arr[i]
    if number > 0:
        positive_integer += 1
    elif number < 0:
        negative_integer += 1
    elif number == 0:
        zero_integer += 1

positive = positive_integer / arr_size
negative = negative_integer / arr_size
zeros = zero_integer / arr_size

print(f'{positive:.6f}')
print(f'{negative:.6f}')
print(f'{zeros:.6f}')