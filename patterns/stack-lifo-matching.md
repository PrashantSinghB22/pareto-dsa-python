# Stack — LIFO Matching

## When to use it

Use a stack when the most recently added/opened item must be processed first.

## Signs to recognize it

- Nested structures
- Matching opening and closing symbols
- "Most recent"
- Reverse order of processing
- Last opened must close first

## Core idea

    opening → push

    closing →
        check top
        match → pop
        mismatch → invalid

    end →
        empty stack = valid

## Example

    "{[()]}"

    { → push
    [ → push
    ( → push
    ) → pop (
    ] → pop [
    } → pop {

    stack empty → valid

## Data structure

Python list:

    append() → push
    pop()    → remove top
    [-1]     → inspect top

## Common mistakes

- Popping before checking for a match.
- Forgetting to check whether the stack is empty.
- Forgetting to check whether the stack is empty at the end.
- Matching brackets without respecting nesting order.

## Complexity

Time: O(n)
Space: O(n)

## Related patterns

- Hash Map / Lookup
- Recursion / Call Stack
- Monotonic Stack
- Expression Evaluation