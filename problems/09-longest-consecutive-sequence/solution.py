# ============================================================
# Problem 09 — Longest Consecutive Sequence
# ============================================================
#
# Given an unsorted array of integers, find the length of the
# longest consecutive elements sequence.
#
# A consecutive sequence consists of integers that increase
# by exactly 1.
#
# Example:
#
#     nums = [100, 4, 200, 1, 3, 2]
#
#     Longest sequence:
#         1, 2, 3, 4
#
#     Answer:
#         4
#
# The optimal solution should run in O(n) average time.
#
# ============================================================


# ============================================================
# Solution — Hash Set ⭐
# ============================================================
#
# Key idea:
#
# Store all numbers in a set so membership checks are O(1)
# on average.
#
# A number can only be the beginning of a sequence if its
# predecessor does not exist.
#
# For example:
#
#     1 → starting point because 0 doesn't exist
#
#     2 → not a starting point because 1 exists
#
#     3 → not a starting point because 2 exists
#
# Once we find a starting point, expand forward:
#
#     1 → 2 → 3 → 4 → ...
#
# Keep track of the longest sequence found.
#
# Time Complexity: O(n) average
# Space Complexity: O(n)
#
# ============================================================

def longest_consecutive(nums):

    numbers = set(nums)
    longest = 0

    for num in numbers:

        # Only start counting if num is the beginning
        # of a consecutive sequence.
        if num - 1 not in numbers:

            current = num
            length = 1

            # Expand the sequence forward.
            while current + 1 in numbers:
                current += 1
                length += 1

            # Update the longest sequence found.
            if length > longest:
                longest = length

    return longest


# ============================================================
# Key Insight
# ============================================================
#
# Don't start a sequence from every number.
#
# Only start when:
#
#     num - 1 does NOT exist
#
# This identifies the beginning of a sequence.
#
# Example:
#
#     [1, 2, 3, 4]
#
#     1 → start
#     2 → skip
#     3 → skip
#     4 → skip
#
# Therefore the sequence is expanded only once.
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Pattern: Hash Set + Sequence Expansion
#
# Recognition clues:
#
# - Need fast membership checks.
# - Numbers are unordered.
# - Need to find consecutive values.
# - Sorting would work but costs O(n log n).
#
# Core idea:
#
#     Put everything in a set.
#
#     Find sequence starts.
#
#     Expand forward from each start.
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([9, 1, 4, 7, 3, 2, 6, 8], 4),
    ([], 0),
    ([1], 1),
    ([1, 2, 3, 4, 5], 5),
    ([100, 200, 300], 1),
    ([1, 1, 1, 2, 2, 3], 3),
]


print("Testing Longest Consecutive Sequence...\n")

for nums, expected in test_cases:

    result = longest_consecutive(nums)

    print(f"Input:    {nums}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")

    assert result == expected

    print("✓ Test passed\n")


print("All tests passed!")