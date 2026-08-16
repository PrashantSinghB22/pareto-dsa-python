# Hash Set + Sequence Expansion

## Pattern Name

Hash Set + Sequence Expansion

## When to use it

Use this pattern when:

- You need fast membership checks.
- The input contains unordered numbers.
- You need to find consecutive values.
- Sorting would solve the problem but costs O(n log n).
- You can identify a starting point and expand from there.

## Signs to recognize it

Look for clues such as:

- "longest consecutive sequence"
- "consecutive integers"
- "does this number exist?"
- "find the next number"
- "unordered array"
- "solve in O(n)"

## Core idea

Put all values into a Hash Set.

Then only start building a sequence when:

    num - 1

does not exist.

That means `num` is the beginning of a sequence.

Then expand:

    num
     ↓
    num + 1
     ↓
    num + 2
     ↓
    ...

until the next number doesn't exist.

## Step-by-step logic

1. Put all numbers into a set.
2. Keep a variable for the longest sequence found.
3. Iterate through the set.
4. Check whether `num - 1` exists.
5. If it exists, skip this number because it isn't a sequence start.
6. If it doesn't exist, start a new sequence.
7. Keep checking `current + 1`.
8. Count the sequence length.
9. Update the longest sequence.
10. Return the longest length.

## Example

Given:

    nums = [100, 4, 200, 1, 3, 2]

Set:

    {100, 4, 200, 1, 3, 2}

Check `1`:

    1 - 1 = 0

    0 doesn't exist.

Therefore `1` is a sequence start.

Expand:

    1 → 2 → 3 → 4

    5 doesn't exist.

Length = 4.

## Why don't we start from every number?

Consider:

    1, 2, 3, 4, 5

If we started from every number:

    1 → 2 → 3 → 4 → 5
    2 → 3 → 4 → 5
    3 → 4 → 5
    4 → 5
    5

We would repeatedly process the same sequence.

Instead:

    1 → 2 → 3 → 4 → 5

Only `1` starts the sequence because:

    1 - 1 = 0

doesn't exist.

## Template

    numbers = set(nums)
    longest = 0

    for num in numbers:

        if num - 1 not in numbers:

            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

## Complexity

Time:

    O(n) average

Space:

    O(n)

The Hash Set uses O(n) space.

Each number is processed a constant number of times on average because sequence expansion begins only at sequence starts.

## Common mistakes

- Starting a sequence from every number.
- Forgetting to check `num - 1`.
- Using a list for membership checks.
- Accidentally using sorting when O(n) is required.
- Forgetting duplicates don't extend a sequence.
- Thinking the nested `while` automatically means O(n²).

## Variations

The same idea can be adapted to:

- Find the actual longest sequence.
- Find all consecutive sequences.
- Find ranges of consecutive values.
- Group values into consecutive runs.

## Related patterns

- Hash Set / Membership
- Hash Map
- Sorting
- Prefix / Suffix Accumulation
- Sliding Window