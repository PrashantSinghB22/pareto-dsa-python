def two_sum_hashmap(nums, target):
  seen = set()

  for i, num in enumerate(nums):
    needed = target - num

    if needed in seen:
      return [seen[needed], i]

    seen[num] = i
