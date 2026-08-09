# Hash Set / Membership Checking

## Pattern

Use a **Hash Set** when you need to quickly determine whether an item has been seen before.

## Recognition Clues

Think Hash Set when you see:

* "contains duplicate"
* "already seen"
* "appears more than once"
* "have we encountered this before?"
* need to track unique values

## Core Idea

```text
item
 ↓
Already in set?
 ↙        ↘
Yes       No
 ↓         ↓
Found    Add it
duplicate
```

## Algorithm

1. Create an empty set.
2. Iterate through the input.
3. Check whether the current item is in the set.
4. If yes → return the required duplicate/found result.
5. If no → add it to the set.
6. Finish processing → return the required result.

## Complexity

```text
Time:  O(n) average
Space: O(n)
```

## Memory Hook

**"Have I seen this before?" → Hash Set**

## Common Mistakes

* Creating the set outside the function.
* Forgetting to add unseen elements.
* Confusing a Set with a Dictionary.
* Claiming `O(1)` space even though the set grows with input.

## Related Patterns

* Frequency Counting
* Hash Map
* Two Pointers
