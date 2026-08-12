# Two Pointers

## When to use it

When comparing or processing elements from opposite ends, or when two positions move through a sequence.

## Signs to recognize it

- Compare first and last elements.
- Move toward the middle.
- Need to process a sequence without extra space.
- Two positions need to move independently.

## Core idea

Maintain two pointers and move them based on the condition.

    left →       ← right

Compare/process → move pointer(s) → repeat.

## Step-by-step

1. Initialize the pointers.
2. Move pointers when elements should be skipped.
3. Compare/process the elements.
4. Update the appropriate pointer(s).
5. Stop when pointers meet/cross.

## Complexity

Usually O(n) time and O(1) extra space.

## Common mistakes

- Moving the wrong pointer.
- Forgetting the stopping condition.
- Moving both pointers when only one should move.
- Returning success before checking the entire sequence.

## Variations

- Same-speed pointers from opposite ends.
- Fast/slow pointers.
- Two pointers moving at different speeds.

## Related patterns

- Track Best State
- Sliding Window
- Hash Set / Lookup