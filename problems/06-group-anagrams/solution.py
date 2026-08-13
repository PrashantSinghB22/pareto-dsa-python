# ============================================================
# Problem 06 — Group Anagrams
# ============================================================
#
# Given a list of strings, group the anagrams together.
#
# Example:
#
# ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# ->
#
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
#
# ============================================================


# ============================================================
# Solution 1 — Sorting + Hash Map
# ============================================================
#
# Idea:
#
# Sort each word to create a canonical signature.
#
# Anagrams produce the same sorted string.
#
#     "eat" -> "aet"
#     "tea" -> "aet"
#     "ate" -> "aet"
#
# Use the signature as the Hash Map key.
#
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
#
# n = number of words
# k = maximum word length
#
# ============================================================

def group_anagrams_sorting(strs):

    groups = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)

    return list(groups.values())


# ============================================================
# Solution 2 — Frequency Counting ⭐ Optimal
# ============================================================
#
# Constraint:
# Words contain lowercase English letters a-z.
#
# Idea:
#
# Instead of sorting each word, count the frequency of each
# character using a fixed array of 26 positions.
#
# The frequency array becomes the word's signature.
#
# Convert the array to a tuple because tuples are immutable
# and can be used as Hash Map keys.
#
#     word
#       ↓
# frequency array
#       ↓
# tuple signature
#       ↓
# Hash Map key
#       ↓
# anagram group
#
# Time Complexity: O(n * k)
# Space Complexity: O(n * k)
#
# ============================================================

def group_anagrams_frequency(strs):

    groups = {}

    for word in strs:

        count = [0] * 26

        for char in word:
            index = ord(char) - ord('a')
            count[index] += 1

        key = tuple(count)

        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)

    return list(groups.values())


# ============================================================
# Key Insight
# ============================================================
#
# Anagrams have identical character frequencies.
#
# Therefore:
#
# same frequency signature → same anagram group
#
# The frequency tuple acts as a canonical representation of
# each word.
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Pattern: Canonical Signature + Hash Map
#
# When to use:
#
# When different objects should be grouped together because
# they share some normalized/canonical representation.
#
# Core idea:
#
#     object → signature → Hash Map key → group
#
# Examples:
#
#     "eat" → frequency signature → group
#     "tea" → same signature      → same group
#
# Related patterns:
#
# - Frequency Counting
# - Hash Map / Lookup
# - Sorting
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]
    ),
    (
        [""],
        [[""]]
    ),
    (
        ["a"],
        [["a"]]
    ),
    (
        ["abc", "bca", "cab", "dog"],
        [
            ["abc", "bca", "cab"],
            ["dog"]
        ]
    ),
]


def normalize(groups):
    """
    Sort each group and then sort the list of groups.
    This lets us compare results regardless of group ordering.
    """
    return sorted([sorted(group) for group in groups])


print("Testing Group Anagrams...\n")

for words, expected in test_cases:

    sorting_result = group_anagrams_sorting(words)
    frequency_result = group_anagrams_frequency(words)

    print(f"Input: {words}")
    print(f"  Sorting:   {sorting_result}")
    print(f"  Frequency: {frequency_result}")

    assert normalize(sorting_result) == normalize(expected)
    assert normalize(frequency_result) == normalize(expected)

    print("  ✓ All solutions passed\n")


print("All tests passed!")