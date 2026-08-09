# ============================================================
# LeetCode 75 — 1768. Merge Strings Alternately
# ============================================================
#
# Given two strings word1 and word2, merge them by taking
# characters alternately, starting with word1.
#
# If one string is longer, append its remaining characters.
#
# Examples:
#
# "abc", "pqr"   → "apbqcr"
# "ab", "pqrs"   → "apbqrs"
# "abcd", "pq"   → "apbqcd"
#
# Constraints:
#
# 1 <= len(word1), len(word2) <= 100
# lowercase English letters
#
# ============================================================


# ============================================================
# Approach — Two Independent Indices
# ============================================================
#
# Idea:
#
# We need to track our current position in BOTH strings.
#
# index1 → current position in word1
# index2 → current position in word2
#
# While either string still has characters:
#
# 1. Take a character from word1 if available.
# 2. Move index1 forward.
# 3. Take a character from word2 if available.
# 4. Move index2 forward.
#
# If one string finishes first, its condition becomes False
# while the other string continues being processed.
#
# Time Complexity: O(n + m)
#
# Space Complexity: O(n + m)
# because the resulting string contains all characters.
#
# Auxiliary Space: O(1), excluding the returned result.
#
# ============================================================


class Solution(object):

    def mergeAlternately(self, word1, word2):
        index1 = 0
        index2 = 0
        result = ""

        while index1 < len(word1) or index2 < len(word2):

            if index1 < len(word1):
                result += word1[index1]
                index1 += 1

            if index2 < len(word2):
                result += word2[index2]
                index2 += 1

        return result


# ============================================================
# Important Insight
# ============================================================
#
# We use TWO indexes because we are independently processing
# TWO different strings.
#
# index1 → "Where am I in word1?"
# index2 → "Where am I in word2?"
#
# The loop continues while at least one string still has
# characters:
#
#     index1 < len(word1) OR index2 < len(word2)
#
# Separate IF statements are important because one string can
# finish before the other.
#
# ============================================================


# ============================================================
# Pattern / Technique
# ============================================================
#
# Two independent indices through two sequences.
#
# This is related to the Two Pointers family, but this problem
# does not require the classic two-pointer interaction pattern.
#
# Do NOT create a new pattern file yet.
#
# ============================================================


# ============================================================
# Local Tests
# ============================================================

test_cases = [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
    ("a", "b", "ab"),
    ("abc", "x", "axbc"),
    ("x", "abc", "xabc"),
]


print("Testing Merge Strings Alternately...\n")

solution = Solution()

for word1, word2, expected in test_cases:
    result = solution.mergeAlternately(word1, word2)

    print(f'word1="{word1}", word2="{word2}"')
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")

    assert result == expected

    print("  ✓ Test passed\n")

print("All tests passed!")