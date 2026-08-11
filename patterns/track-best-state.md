# Track Best State

## When to use it

When processing data left-to-right and only the best previous
value/state matters for making the current decision.

## Signs to recognize it

- Need the best/minimum/maximum value seen so far.
- Current result depends on previous values.
- Brute force compares many pairs.
- Can summarize previous information with one variable.

## Core idea

Maintain useful state while scanning once.

Example:

minimum_price → cheapest value seen so far
best_profit   → best result seen so far

## Step-by-step

1. Initialize the state.
2. Process each element.
3. Use previous state to calculate the current result.
4. Update the best result.
5. Update the state.
6. Continue.

## Complexity

Usually O(n) time and O(1) extra space.

## Common mistakes

- Using information from the future.
- Updating state in the wrong order.
- Tracking more information than necessary.

## Variations

- Track minimum.
- Track maximum.
- Track best score.
- Track running sum/count/state.

## Related patterns

- Hash Map / Lookup
- Sliding Window
- Prefix Sum