from statistics import median

arr = [0, 1, 2, 4, 6, 5, 3]
sorted_array = sorted(arr)
len_list = len(arr)

if len_list % 2 == 1:
    median = sorted_array[len_list // 2]
else:
    med1 = sorted_array[len_list // 2]
    med2 = sorted_array[len_list // 2 - 1]
    median = (med1+med2) / 2


print(median)