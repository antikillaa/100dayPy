arr = [1, 3, 5, 7, 9]
arr_min = arr.copy()

min_value = min(arr)
max_value = max(arr)

arr.remove(max_value)
arr_min.remove(min_value)

print(f'{sum(arr)} {sum(arr_min)}')
