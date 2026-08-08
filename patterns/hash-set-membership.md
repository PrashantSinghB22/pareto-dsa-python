# Hash Set / Membership Checking

## Pattern Name

Hash Set / Membership Checking

## When to Use

Use this pattern when you need to efficiently determine whether:

- a value has appeared before
- a value already exists
- a duplicate exists
- an element is unique
- an item has already been processed

## Recognition Clues

Look for phrases such as:

- "contains duplicate"
- "appears more than once"
- "already seen"
- "have we encountered this before?"
- "does this value exist?"

## Core Idea

Maintain a set of values that have already been encountered.

For every new value:

1. Check whether it is already in the set.
2. If yes → the required condition has been found.
3. If no → add it to the set.
4. Continue.

## Typical Complexity

Time: O(n) average

Space: O(n)

## Memory Hook

> "Have I seen this before?" → Think Hash Set.

## Example

Input:

[5, 3, 8, 2, 5]

Process:

5 → not seen → add
3 → not seen → add
8 → not seen → add
2 → not seen → add
5 → already seen → duplicate

Result:

True

## Related Patterns

- Hash Map
- Frequency Counting
- Two Sum
- Sliding Window
- Membership Checking