# ============================================================
# Problem 08 — Valid Parentheses
# ============================================================
#
# Given a string containing the characters:
#
#     ( ) { } [ ]
#
# determine whether the brackets are valid.
#
# A valid string must satisfy:
#
# 1. Every opening bracket has a corresponding closing bracket.
# 2. Brackets close in the correct order.
# 3. Every closing bracket matches the most recently opened
#    unmatched bracket.
#
# Examples:
#
#     "()"       -> True
#     "()[]{}"   -> True
#     "{[]}"     -> True
#     "(]"       -> False
#     "([)]"     -> False
#
# ============================================================


# ============================================================
# Solution — Stack + Hash Map ⭐
# ============================================================
#
# Key idea:
#
# The most recently opened bracket must be the first one
# closed.
#
# This is Last In, First Out (LIFO), which makes a stack the
# natural data structure.
#
# Opening bracket:
#
#     push onto stack
#
# Closing bracket:
#
#     1. Make sure the stack isn't empty.
#     2. Check whether the top matches.
#     3. If it matches, pop it.
#     4. Otherwise, the string is invalid.
#
# The dictionary tells us which opening bracket each closing
# bracket expects:
#
#     ")" -> "("
#     "]" -> "["
#     "}" -> "{"
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# ============================================================

def is_valid(s):

    stack = []

    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:

        # Opening bracket → remember it.
        if char in mapping.values():
            stack.append(char)

        # Closing bracket → validate it.
        else:

            # Nothing available to match this closing bracket.
            if not stack:
                return False

            # Most recent opening bracket doesn't match.
            if stack[-1] != mapping[char]:
                return False

            # Correctly matched → remove the opening bracket.
            stack.pop()

    # Valid only if every opening bracket was closed.
    return not stack


# ============================================================
# Key Insight
# ============================================================
#
# The problem is fundamentally about nesting.
#
# The most recently opened bracket must be closed first.
#
# Therefore:
#
#     opening → push
#
#     closing →
#         check top
#         match → pop
#         mismatch → False
#
#     end →
#         empty stack → True
#         non-empty stack → False
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Pattern: Stack / LIFO Matching
#
# Recognition clue:
#
# If something must be processed in the reverse order it was
# opened or added, think:
#
#     Stack → LIFO
#
# Common examples:
#
# - Parentheses matching
# - Nested brackets
# - Undo operations
# - Browser history
# - Function call stack
# - Expression evaluation
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("{[]}", True),
    ("(]", False),
    ("([)]", False),
    ("{[()]}", True),
    ("(", False),
    (")", False),
    ("", True),
    ("((()))", True),
    ("(((", False),
    ("())", False),
]


print("Testing Valid Parentheses...\n")

for s, expected in test_cases:

    result = is_valid(s)

    print(f"Input:    {s!r}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")

    assert result == expected

    print("✓ Test passed\n")


print("All tests passed!")