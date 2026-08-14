# ============================================================
# Problem 07 — Product of Array Except Self
# ============================================================
#
# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all elements of nums
# except nums[i].
#
# The optimal solution must:
# - Run in O(n) time
# - Use O(1) extra space (excluding the output array)
# - Not use division
#
# ============================================================


# ============================================================
# Solution 1 — Brute Force
# ============================================================
#
# Idea:
#
# For every index i, iterate through the entire array and
# multiply every element except nums[i].
#
# Time Complexity: O(n²)
# Space Complexity: O(n) for the output array
#
# ============================================================

def product_except_self_brute(nums):

    result = []

    for i in range(len(nums)):
        product = 1

        for j in range(len(nums)):
            if i != j:
                product = product * nums[j]

        result.append(product)

    return result


# ============================================================
# Solution 2 — Prefix + Suffix Products ⭐ Optimal
# ============================================================
#
# Idea:
#
# For every index:
#
# answer = product of everything to the LEFT
#        × product of everything to the RIGHT
#
# First pass:
# Store prefix products in the result array.
#
# Second pass:
# Traverse from right to left while maintaining a running
# suffix product and multiply it into result[i].
#
# Time Complexity: O(n)
# Space Complexity: O(1) extra space
# (excluding the required output array)
#
# ============================================================

def product_except_self(nums):

    result = [1] * len(nums)

    # Build prefix products.
    prefix = 1

    for i in range(len(nums)):
        result[i] = prefix
        prefix = prefix * nums[i]

    # Build suffix products and combine them with prefixes.
    suffix = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * suffix
        suffix = suffix * nums[i]

    return result


# ============================================================
# Key Insight
# ============================================================
#
# Instead of repeatedly calculating:
#
#     "multiply everything except nums[i]"
#
# break the problem into:
#
#     LEFT PRODUCT × RIGHT PRODUCT
#
# First pass:
#
#     result[i] = product of everything before i
#
# Second pass:
#
#     suffix = product of everything after i
#
#     result[i] *= suffix
#
# This gives O(n) time without using division.
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([2, 3, 4, 5], [60, 40, 30, 24]),
    ([0, 1, 2, 3], [6, 0, 0, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([5], [1]),
]


print("Testing Product of Array Except Self...\n")

for nums, expected in test_cases:

    brute_result = product_except_self_brute(nums)
    optimal_result = product_except_self(nums)

    print(f"Input:    {nums}")
    print(f"Brute:    {brute_result}")
    print(f"Optimal:  {optimal_result}")
    print(f"Expected: {expected}")

    assert brute_result == expected
    assert optimal_result == expected

    print("✓ Test passed\n")


print("All tests passed!")