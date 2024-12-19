matrix = [[1, 2, 3],
          [4, 5, 6],
          [9, 8, 9]]
right_sum = 0
left_sum = 0

for i in range(len(matrix)):
    right_sum += matrix[i][i]
    left_sum += matrix[i][len(matrix) -1 -i]


print(abs(right_sum-left_sum))
