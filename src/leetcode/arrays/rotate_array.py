def rotate(nums, n):
    for i in range(n):
        t = nums[-1]
        nums.pop(-1)
        nums.insert(0, t)


arr = [1, 2, 3, 4, 5, 6, 7]

rotate(arr, 4)

print(arr)
