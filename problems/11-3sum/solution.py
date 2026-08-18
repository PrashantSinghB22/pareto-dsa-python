# ============================================================
# Problem 11 — 3Sum
# ============================================================
#
# Given an integer array nums, find all unique triplets
# [a, b, c] such that:
#
#     a + b + c == 0
#
# The result must not contain duplicate triplets.
#
# ============================================================


def three_sum(nums):
    results = []

    # Sorting gives us:
    # 1. Two-pointer movement
    # 2. Adjacent duplicate values
    nums = sorted(nums)

    # We need at least two elements after i
    # to form a triplet.
    for i in range(len(nums) - 2):

        # Skip duplicate first values so we don't
        # produce the same triplet multiple times.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

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

            # Sum is too small → increase it.
            if current_sum < target:
                left += 1

            # Sum is too large → decrease it.
            elif current_sum > target:
                right -= 1

            # Found a valid triplet.
            else:
                results.append([
                    nums[i],
                    nums[left],
                    nums[right]
                ])

                # Move both pointers to search for
                # another pair.
                left += 1
                right -= 1

                # Skip duplicate left values.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate right values.
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return results


# ============================================================
# Tests
# ============================================================

test_cases = [
    (
        [-1, 0, 1, 2, -1, -4],
        [[-1, -1, 2], [-1, 0, 1]]
    ),
    (
        [0, 1, 1],
        []
    ),
    (
        [0, 0, 0],
        [[0, 0, 0]]
    ),
    (
        [-2, 0, 0, 2, 2],
        [[-2, 0, 2]]
    ),
    (
        [1, 2, -2, -1],
        []
    ),
]


print("Testing 3Sum...\n")

for nums, expected in test_cases:
    result = three_sum(nums)

    # Sort both so ordering doesn't matter.
    result = sorted(result)
    expected = sorted(expected)

    print(f"Input:    {nums}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")

    assert result == expected

    print("✓ Test passed\n")


print("All tests passed!")