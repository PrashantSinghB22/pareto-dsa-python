# ============================================================
# Problem 02 — Valid Anagram
# ============================================================
#
# Given two strings s and t, determine whether t is an
# anagram of s.
#
# An anagram contains the same characters with the same
# frequencies, but the characters may appear in a different order.
#
# Examples:
#
# "anagram" + "nagaram" -> True
# "rat"     + "car"     -> False
#
# ============================================================


# ============================================================
# Solution 1 — Sorting
# ============================================================
#
# Idea:
# If two strings are anagrams, sorting both strings will produce
# the same sequence of characters.
#
# Example:
#
#     "race" → "acer"
#     "care" → "acer"
#
# Since the sorted strings are equal, they are anagrams.
#
# Time Complexity: O(n log n)
# Space Complexity: Depends on Python's sorting implementation
#
# ============================================================

def valid_anagram_sorting(s, t):
    if len(s) != len(t):
        return False

    sorted_s = ''.join(sorted(s))
    sorted_t = ''.join(sorted(t))

    return sorted_s == sorted_t


# ============================================================
# Solution 2 — Hash Map / Dictionary
# ============================================================
#
# Idea:
# Count the frequency of every character in both strings.
#
# If the frequency tables are identical, the strings are
# anagrams.
#
# Example:
#
#     "aab"
#
#     a → 2
#     b → 1
#
# Time Complexity: O(n) average
# Space Complexity: O(n)
#
# ============================================================

def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}

    for char in s:
        if char not in s_count:
            s_count[char] = 1
        else:
            s_count[char] += 1

    for char in t:
        if char not in t_count:
            t_count[char] = 1
        else:
            t_count[char] += 1

    return s_count == t_count


# ============================================================
# Solution 3 — Fixed Array ⭐ Optimal Under a-z Constraint
# ============================================================
#
# Constraint:
#
# The input contains only lowercase English letters a-z.
#
# Idea:
#
# There are only 26 possible characters, so we can use an array
# of 26 counters instead of a dictionary.
#
# For every character in s:
#
#     increase its counter
#
# For every character in t:
#
#     decrease its counter
#
# If every counter ends at zero, the strings contain exactly
# the same characters with exactly the same frequencies.
#
# Character → Array Index:
#
#     'a' → 0
#     'b' → 1
#     'c' → 2
#     ...
#     'z' → 25
#
# We calculate the index using:
#
#     ord(char) - ord('a')
#
# This converts the character into its distance from 'a'.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# ============================================================

def valid_anagram_array(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26

    for char in s:
        index = ord(char) - ord('a')
        count[index] += 1

    for char in t:
        index = ord(char) - ord('a')
        count[index] -= 1

    for value in count:
        if value != 0:
            return False

    return True


# ============================================================
# Key Insight
# ============================================================
#
# Anagram problems are not about character existence.
#
# They are about character FREQUENCY.
#
# Example:
#
#     "aab"
#     "abb"
#
# Both contain 'a' and 'b', but their frequencies differ:
#
#     a → 2 vs 1
#     b → 1 vs 2
#
# Therefore they are not anagrams.
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Pattern Name:
# Frequency Counting
#
# Recognition Clues:
#
#     - frequency
#     - occurrences
#     - how many times
#     - same characters
#     - same elements with the same counts
#
# Core Idea:
#
#     item → frequency
#
# Data Structure Choice:
#
#     Small fixed domain → Fixed Array
#     Flexible/unknown domain → Hash Map
#
# ============================================================


# ============================================================
# Solution Comparison
# ============================================================
#
# Approach          Time          Space
# ------------------------------------------------------------
# Sorting           O(n log n)    Depends on sorting
# Dictionary        O(n) avg      O(n)
# Fixed Array       O(n)          O(1)  ⭐
#
# The Fixed Array is optimal when the input is restricted to
# lowercase English letters a-z because there are only 26
# possible characters.
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aab", "abb", False),
    ("race", "care", True),
    ("", "", True),
    ("a", "b", False),
    ("listen", "silent", True),
]


print("Testing Valid Anagram solutions...\n")

for s, t, expected in test_cases:
    sorting_result = valid_anagram_sorting(s, t)
    dictionary_result = valid_anagram(s, t)
    array_result = valid_anagram_array(s, t)

    print(f's="{s}", t="{t}"')
    print(f"  Sorting:    {sorting_result}")
    print(f"  Dictionary: {dictionary_result}")
    print(f"  Array:      {array_result}")
    print(f"  Expected:   {expected}")

    assert sorting_result == expected
    assert dictionary_result == expected
    assert array_result == expected

    print("  ✓ All solutions passed\n")

print("All tests passed!")