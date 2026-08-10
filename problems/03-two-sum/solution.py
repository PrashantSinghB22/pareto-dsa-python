# ============================================================
# Problem 03 — Two Sum
# ============================================================
#
# Given an array of integers nums and an integer target,
# return the indices of the two numbers whose sum equals target.
#
# Each input has exactly one solution, and the same element
# cannot be used twice.
#
# Examples:
#
# [2, 7, 11, 15], target = 9  -> [0, 1]
# [3, 2, 4], target = 6       -> [1, 2]
# [3, 3], target = 6          -> [0, 1]
#
# ============================================================


# ============================================================
# Solution 1 — Brute Force
# ============================================================
#
# Idea:
#
# Try every possible pair of numbers.
#
# For each index i, compare nums[i] with every element
# after it using index j.
#
# If their sum equals target, return their indices.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#
# ============================================================

def two_sum_brute(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return [i, j]


# ============================================================
# Solution 2 — Hash Map ⭐ Optimal
# ============================================================
#
# Idea:
#
# Instead of checking every pair, calculate the number we need:
#
#     needed = target - current
#
# Store previously seen numbers in a dictionary:
#
#     number -> index
#
# If "needed" is already in the dictionary, we have found
# the pair and can immediately return its two indices.
#
# Example:
#
# nums = [2, 7, 11, 15]
# target = 9
#
# Start:
# seen = {}
#
# current = 2
# needed = 9 - 2 = 7
# 7 not seen → store 2: 0
#
# current = 7
# needed = 9 - 7 = 2
# 2 is already seen at index 0
#
# return [0, 1]
#
# Time Complexity: O(n) average
# Space Complexity: O(n)
#
# ============================================================

def two_sum_hashmap(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i


# ============================================================
# Key Insight
# ============================================================
#
# Brute Force asks:
#
#     "Which pair adds up to target?"
#
# Hash Map asks:
#
#     "What number do I need?"
#     needed = target - current
#
# Then:
#
#     "Have I already seen that number?"
#
# The dictionary stores:
#
#     value -> index
#
# This is different from Contains Duplicate:
#
# Contains Duplicate:
#     Set → value existence
#
# Two Sum:
#     Hash Map → value + associated index
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Hash Map / Lookup
#
# Recognition clues:
#
# - Need to find a matching value quickly.
# - Need information associated with a previously seen value.
# - "Have I seen the value I need?"
# - Need to map a value to its index/frequency/etc.
#
# Memory Hook:
#
#     "I need the value AND information about it."
#     → Hash Map
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
]


print("Testing Two Sum...\n")

for nums, target, expected in test_cases:

    brute_result = two_sum_brute(nums, target)
    hashmap_result = two_sum_hashmap(nums, target)

    print(f"nums={nums}, target={target}")
    print(f"  Brute Force: {brute_result}")
    print(f"  Hash Map:    {hashmap_result}")
    print(f"  Expected:    {expected}")

    assert brute_result == expected
    assert hashmap_result == expected

    print("  ✓ All solutions passed\n")


print("All tests passed!")