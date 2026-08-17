# ============================================================
# Problem 10 — Container With Most Water
# ============================================================
#
# Given an array of heights, choose two vertical lines that
# form a container capable of holding the maximum amount of
# water.
#
# For two lines at indices left and right:
#
#     width = right - left
#     height = min(height[left], height[right])
#
#     area = width * height
#
# The goal is to maximize the area.
#
# ============================================================


# ============================================================
# Solution — Two Pointers ⭐
# ============================================================
#
# Start with the widest possible container:
#
#     left  = 0
#     right = len(height) - 1
#
# At every step:
#
# 1. Calculate the current area.
# 2. Update max_area if the current area is larger.
# 3. Move the pointer belonging to the shorter line.
#
# Why move the shorter line?
#
# The shorter line is the bottleneck.
#
# If we move the taller line instead:
#
#     width decreases
#     shorter height remains the limiting factor
#
# Therefore, moving the taller line cannot produce a better
# container. We need to move the shorter line to have a chance
# of finding a taller boundary.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# ============================================================


def max_water(height):
    max_area = 0

    left = 0
    right = len(height) - 1

    while left < right:

        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height

        if area > max_area:
            max_area = area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# ============================================================
# Key Insight
# ============================================================
#
# Area is:
#
#     width × shorter_height
#
# Starting with the two outermost lines gives us the maximum
# possible width.
#
# Once we calculate that area, we move the shorter line.
#
# The shorter line is the bottleneck. Moving the taller line
# would reduce width without allowing the limiting height to
# improve.
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Pattern: Two Pointers
#
# Recognition clues:
#
# - Two ends of an array/string matter.
# - We can make progress by moving one pointer.
# - A decision tells us which pointer to move.
# - We want to avoid examining every possible pair.
#
# Here:
#
#     shorter left line  → move left
#     shorter right line → move right
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([1, 2, 1], 2),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 3, 4, 5], 6),
    ([5, 4, 3, 2, 1], 6),
    ([10, 1, 1, 1, 10], 40),
]


print("Testing Container With Most Water...\n")

for heights, expected in test_cases:

    result = max_water(heights)

    print(f"Input:    {heights}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")

    assert result == expected

    print("✓ Test passed\n")


print("All tests passed!")