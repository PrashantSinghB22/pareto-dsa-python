# ============================================================
# Problem 01 — Contains Duplicate
# ============================================================
#
# Given an integer array nums, determine whether any value
# appears at least twice in the array.
#
# Return True if a duplicate exists.
# Return False if every element is unique.
#
# Examples:
#
# [1, 2, 3, 1] -> True
# [1, 2, 3, 4] -> False
# [1, 1]       -> True
#
# ============================================================


# ============================================================
# Solution 1 — Brute Force
# ============================================================
#
# Idea:
# Compare every number with every number that comes after it.
#
# If two numbers are equal, a duplicate exists.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#
# Why?
# In the worst case, we compare many pairs of elements.
# We don't use any additional data structure.
#
# ============================================================

def contains_duplicate_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# ============================================================
# Solution 2 — Hash Set ⭐ Optimal
# ============================================================
#
# Idea:
# Keep track of the numbers we have already seen.
#
# For every number:
#
#   If it is already in the set:
#       duplicate found → True
#
#   Otherwise:
#       add it to the set
#
# If we finish the entire array without finding a duplicate,
# return False.
#
# Time Complexity: O(n) average
# Space Complexity: O(n)
#
# Why?
# Hash Set membership checking is O(1) average.
# The set can contain up to n unique elements.
#
# ============================================================

def contains_duplicate_hashset(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)

    return False


# ============================================================
# Key Insight
# ============================================================
#
# The important question is:
#
#     "Have I seen this value before?"
#
# This naturally suggests a Hash Set.
#
# Hash Set:
#
#     value → existence
#
# Frequency Map:
#
#     value → count
#
# We only need to know whether a value has appeared,
# so a Hash Set is enough.
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Pattern Name:
# Hash Set / Membership Checking
#
# Recognition Clue:
#
#     "Have I seen this before?"
#
# Core Idea:
#
#     Store previously seen values.
#     Check membership before processing the current value.
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1], True),
    ([1, 2, 3, 4, 5, 6, 7, 7, 2], True),
    ([], False),
    ([5], False),
]


print("Testing Contains Duplicate solutions...\n")

for nums, expected in test_cases:
    brute_result = contains_duplicate_brute(nums)
    hashset_result = contains_duplicate_hashset(nums)

    print(f"nums = {nums}")
    print(f"  Brute Force: {brute_result}")
    print(f"  Hash Set:    {hashset_result}")
    print(f"  Expected:    {expected}")

    assert brute_result == expected
    assert hashset_result == expected

    print("  ✓ All solutions passed\n")

print("All tests passed!")