def remove_duplicates_set(nums):
    if len(nums) == 0:
        return 0

    no_dup_set = list(set(nums))
    return no_dup_set


def remove_duplicates_naive(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(int(i))
    return res


nums = [1, 2, 3, 2, 3, 3]

no_duplicates_set = remove_duplicates_naive(nums)

no_duplicates_naive = remove_duplicates_naive(nums)

print(no_duplicates_set)
print(no_duplicates_naive)
