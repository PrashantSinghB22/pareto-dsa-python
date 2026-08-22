# Matrix Validation with Hash Sets

## When to use it

Use this pattern when a matrix has multiple independent
constraints that must be checked while scanning each cell.

## Signs to recognize it

- "No duplicates in each row"
- "No duplicates in each column"
- "No duplicates in each region/box"
- Need fast membership checking
- Matrix has multiple independent validation rules

## Core idea

Give each constraint its own set.

For Sudoku:

cell
↓
row set
column set
box set

Check all three before inserting the value.

## Step-by-step logic

1. Create a set for every row.
2. Create a set for every column.
3. Create a set for every box.
4. Visit every cell.
5. Ignore empty cells.
6. Determine the cell's box.
7. Check whether the value already exists in its row, column, or box.
8. If it does, return False.
9. Otherwise add it to all three sets.
10. If the entire board is processed, return True.

## Box mapping

For a 9 × 9 Sudoku board:

box = (row // 3) * 3 + (column // 3)

## Common mistakes

- Forgetting to skip empty cells.
- Checking only rows and columns.
- Using lists instead of sets for membership checking.
- Using `.append()` on a set instead of `.add()`.
- Mixing up row and column indices.
- Forgetting that multiple cells belong to the same 3 × 3 box.

## Related patterns

- Hash Set / Membership Checking
- Matrix Traversal
- Frequency Counting