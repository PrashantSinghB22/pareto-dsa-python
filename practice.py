def two_sum_hashmap(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i


print(two_sum_hashmap([1,4,5,6,3], 11))