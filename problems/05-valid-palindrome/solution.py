# ============================================================
# Problem 05 — Valid Palindrome
# ============================================================
#
# Given a string s, determine whether it is a palindrome after:
# - converting uppercase letters to lowercase
# - ignoring non-alphanumeric characters
#
# Examples:
#
# "A man, a plan, a canal: Panama" -> True
# "race a car"                     -> False
# " "                              -> True
#
# ============================================================


# ============================================================
# Solution 1 — Clean + Reverse
# ============================================================
#
# Idea:
#
# Create a cleaned version containing only alphanumeric
# characters in lowercase, then compare it with its reverse.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# ============================================================

def is_palindrome_brute(s):

    new_s = ""

    for char in s:
        if char.isalnum():
            new_s += char.lower()

    return new_s == new_s[::-1]


# ============================================================
# Solution 2 — Two Pointers ⭐ Optimal
# ============================================================
#
# Idea:
#
# Use two pointers starting at opposite ends of the string.
#
# Skip non-alphanumeric characters.
# Compare valid characters case-insensitively.
#
# If any pair doesn't match, return False.
#
# If all pairs match, return True.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# ============================================================

def is_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ============================================================
# Key Insight
# ============================================================
#
# We don't need to build a cleaned string.
#
# Instead:
#
# left  -> finds the next valid character from the left
# right -> finds the next valid character from the right
#
# Then compare:
#
#     s[left].lower() == s[right].lower()
#
# A mismatch means False immediately.
# If the pointers meet/cross without a mismatch, return True.
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
# - Comparing opposite ends of a sequence.
# - Moving inward toward the middle.
# - Need to compare pairs from both ends.
# - Can solve the problem without creating another sequence.
#
# Core idea:
#
#     left →        ← right
#
# Compare, then move both pointers inward.
#
# Common variations:
#
# - Palindrome checking
# - Pair searching in sorted arrays
# - Reversing arrays
# - Removing elements from both ends
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("a", True),
    ("ab", False),
    ("aba", True),
    ("abba", True),
    ("abcba", True),
    ("0P", False),
    ("Madam", True),
]


print("Testing Valid Palindrome...\n")

for s, expected in test_cases:

    brute_result = is_palindrome_brute(s)
    optimal_result = is_palindrome(s)

    print(f's="{s}"')
    print(f"  Brute:   {brute_result}")
    print(f"  Optimal: {optimal_result}")
    print(f"  Expected: {expected}")

    assert brute_result == expected
    assert optimal_result == expected

    print("  ✓ All solutions passed\n")


print("All tests passed!")