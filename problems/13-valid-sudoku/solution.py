# ============================================================
# Problem 13 — Valid Sudoku
# ============================================================
#
# Problem:
#
# Determine if a given 9 x 9 Sudoku board is valid.
#
# A Sudoku board is valid if:
#
# 1. Each row contains no duplicate digits from 1 to 9.
# 2. Each column contains no duplicate digits from 1 to 9.
# 3. Each 3 x 3 sub-box contains no duplicate digits from 1 to 9.
#
# Empty cells are represented by ".".
#
# The board does not need to be completely solved.
# We only need to determine whether the current board is valid.
#
# Example 1:
#
# board =
# [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
#
# Output:
#
# True
#
# Example 2:
#
# board =
# [
#     ["8","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
#
# Output:
#
# False
#
# Explanation:
#
# The first column contains two "8"s.
#
# Constraints:
#
# - The board is exactly 9 x 9.
# - Each cell contains "." or a digit from "1" to "9".
#
# ============================================================


def is_valid_sudoku(board):
    # Each row gets its own set.
    rows = [set() for _ in range(9)]

    # Each column gets its own set.
    columns = [set() for _ in range(9)]

    # Each 3 x 3 box gets its own set.
    boxes = [set() for _ in range(9)]

    # Visit every cell in the board.
    for r in range(9):
        for c in range(9):
            num = board[r][c]

            # Empty cells do not need to be checked.
            if num == ".":
                continue

            # Determine which 3 x 3 box this cell belongs to.
            box = (r // 3) * 3 + (c // 3)

            # If the number already exists in its row,
            # column, or box, the board is invalid.
            if (
                num in rows[r]
                or num in columns[c]
                or num in boxes[box]
            ):
                return False

            # Record the number in all three places.
            rows[r].add(num)
            columns[c].add(num)
            boxes[box].add(num)

    return True


# ============================================================
# Tests
# ============================================================

test_cases = [
    (
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        True
    ),
    (
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        False
    ),
    (
        [
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."]
        ],
        True
    ),
]


print("Testing Valid Sudoku...\n")

for board, expected in test_cases:
    result = is_valid_sudoku(board)

    print(f"Result:   {result}")
    print(f"Expected: {expected}")

    assert result == expected

    print("✓ Test passed\n")


print("All tests passed!")