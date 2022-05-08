def single_number(arr):
    if len(arr) == 0:
        return 0
    result = 0
    for n in arr:
        result ^= n
    return result


arr = [4,1,2,1,2]
print(single_number(arr))
