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

## Variation — 3Sum

### When to use it

When a problem asks for three values satisfying a sum condition
and duplicate combinations must be avoided.

### Core idea

Sort the array.

Fix one element.

Use two pointers on the remaining portion.

### Logic

1. Sort the array.
2. Fix `nums[i]`.
3. Set `left = i + 1`.
4. Set `right = len(nums) - 1`.
5. Target becomes `-nums[i]`.
6. If the two-pointer sum is too small, move `left`.
7. If too large, move `right`.
8. If equal, record the triplet.
9. Skip duplicates.

### Important duplicate distinction

Do not blindly skip every duplicate value.

A duplicate value may be necessary:

[-1, -1, 2]

is a valid triplet.

We skip duplicates when they would cause us to produce
the same triplet again.

### Related problems

- Two Sum
- 3Sum
- 4Sum
- Two Pointers
- Sort + Two Pointers

## Related patterns

- Track Best State
- Sliding Window
- Hash Set / Lookup