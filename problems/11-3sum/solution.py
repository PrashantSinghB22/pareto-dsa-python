# ============================================================
# Problem 11 — 3Sum
# ============================================================
#
# Problem:
#
# Given an integer array nums, return all the unique triplets
# [nums[i], nums[j], nums[k]] such that:
#
#     i != j
#     i != k
#     j != k
#
# and:
#
#     nums[i] + nums[j] + nums[k] == 0
#
# The solution must not contain duplicate triplets.
#
# The order of the triplets and the order of the numbers
# inside each triplet does not matter.
#
# Example 1:
#
# nums = [-1, 0, 1, 2, -1, -4]
#
# Output:
#
# [
#     [-1, -1, 2],
#     [-1, 0, 1]
# ]
#
# Explanation:
#
# -1 + -1 + 2 = 0
# -1 + 0 + 1 = 0
#
# Example 2:
#
# nums = [0, 1, 1]
#
# Output:
#
# []
#
# Explanation:
#
# There are no three numbers that add up to 0.
#
# Example 3:
#
# nums = [0, 0, 0]
#
# Output:
#
# [
#     [0, 0, 0]
# ]
#
# Explanation:
#
# Even though there are multiple ways to choose three zeros,
# the same triplet should only appear once.
#
# Constraints:
#
# - 3 <= nums.length <= 3000
# - -10^5 <= nums[i] <= 10^5
#
# ============================================================


def three_sum(nums):
    nums = sorted(nums)
    result = []

    # Fix one number at a time.
    for i in range(len(nums) - 2):

        # Skip duplicate first numbers.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Search for the other two numbers.
        left = i + 1
        right = len(nums) - 1

        # We need:
        #
        # nums[i] + nums[left] + nums[right] = 0
        #
        # Therefore:
        #
        # nums[left] + nums[right] = -nums[i]
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            # Sum is too small.
            if current_sum < target:
                left += 1

            # Sum is too large.
            elif current_sum > target:
                right -= 1

            # Found a valid triplet.
            else:
                result.append([
                    nums[i],
                    nums[left],
                    nums[right]
                ])

                # Move both pointers to search for
                # another possible pair.
                left += 1
                right -= 1

                # Skip duplicate left values.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate right values.
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


# ============================================================
# Tests
# ============================================================

test_cases = [
    (
        [-1, 0, 1, 2, -1, -4],
        [
            [-1, -1, 2],
            [-1, 0, 1]
        ]
    ),
    (
        [0, 1, 1],
        []
    ),
    (
        [0, 0, 0],
        [
            [0, 0, 0]
        ]
    ),
    (
        [-2, 0, 0, 2, 2],
        [
            [-2, 0, 2]
        ]
    ),
    (
        [1, 2, -2, -1],
        []
    ),
]


print("Testing 3Sum...\n")

for nums, expected in test_cases:
    result = three_sum(nums)

    # Sort both results so the order of triplets
    # does not affect the test.
    result = sorted(result)
    expected = sorted(expected)

    print(f"Input:    {nums}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")

    assert result == expected

    print("✓ Test passed\n")


print("All tests passed!")