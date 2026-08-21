# ============================================================
# Problem 12 — Top K Frequent Elements
# ============================================================
#
# Problem:
#
# Given an integer array nums and an integer k, return the k
# most frequent elements.
#
# You may return the answer in any order.
#
# In other words, find the k numbers that appear most often
# in nums.
#
# Example 1:
#
# nums = [1,1,1,2,2,3]
# k = 2
# Output = [1,2]
#
# Explanation:
# 1 appears 3 times.
# 2 appears 2 times.
# 3 appears 1 time.
#
# Therefore, the 2 most frequent elements are [1,2].
#
# Example 2:
#
# nums = [1]
# k = 1
# Output = [1]
#
# Example 3:
#
# nums = [1,2,1,2,1,2,3,1,3,2]
# k = 2
# Output = [1,2]
#
# Constraints:
#
# - 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
# - 1 <= k <= number of unique elements in nums
# - The answer is guaranteed to be unique.
#
# ============================================================


def top_k_frequent(nums, k):
    count = {}

    # Count the frequency of each number.
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    # Create buckets where the index represents frequency.
    # Each bucket contains the numbers with that frequency.
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, frequency in count.items():
        buckets[frequency].append(num)

    result = []

    # Start from the highest frequency and work downward.
    for frequency in range(len(nums), 0, -1):
        for num in buckets[frequency]:
            result.append(num)

            # Stop once we have k elements.
            if len(result) == k:
                return result

    return result


# ============================================================
# Tests
# ============================================================

test_cases = [
    (
        [1, 1, 1, 2, 2, 3],
        2,
        {1, 2}
    ),
    (
        [1],
        1,
        {1}
    ),
    (
        [1, 2, 1, 2, 1, 2, 3, 1, 3, 2],
        2,
        {1, 2}
    ),
    (
        [-1, -1, -1, 2, 2, 3],
        2,
        {-1, 2}
    ),
]


print("Testing Top K Frequent Elements...\n")

for nums, k, expected in test_cases:
    result = top_k_frequent(nums, k)

    print(f"Input:    nums={nums}, k={k}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")

    assert set(result) == expected
    assert len(result) == k

    print("✓ Test passed\n")


print("All tests passed!")