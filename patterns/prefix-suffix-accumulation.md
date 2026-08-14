# Prefix / Suffix Accumulation

## When to use it

Use this pattern when the answer for each position depends on information from:

- everything before the current position
- everything after the current position
- or both

## Signs to recognize it

Look for problem statements involving:

- "all elements before..."
- "all elements after..."
- "everything except the current element"
- calculating something for every index using surrounding elements

## Core idea

Break the problem into two directions:

    LEFT → RIGHT
    accumulate prefix information

    RIGHT → LEFT
    accumulate suffix information

Then combine the two.

For Product of Array Except Self:

    answer[i]
        =
    prefix product × suffix product

## Step-by-step logic

1. Create the output array.
2. Traverse from left to right.
3. Store the product of everything before each index.
4. Traverse from right to left.
5. Maintain a running suffix product.
6. Multiply the suffix product into the output.
7. Return the output.

## Example

For:

    nums = [1, 2, 3, 4]

Prefix products:

    [1, 1, 2, 6]

Suffix products:

    [24, 12, 4, 1]

Combine:

    [1×24, 1×12, 2×4, 6×1]

Result:

    [24, 12, 8, 6]

## Template

    prefix = identity

    for i from left to right:
        use prefix
        update prefix using current element

    suffix = identity

    for i from right to left:
        combine suffix with result
        update suffix using current element

## Complexity

Usually:

    Time: O(n)
    Extra Space: O(1)

when the output array can be reused to store one direction of accumulated information.

## Common mistakes

- Updating prefix before storing it.
- Updating suffix before using it.
- Traversing the second pass in the wrong direction.
- Forgetting the identity value.
- Accidentally creating unnecessary prefix and suffix arrays.

## Important concept

The identity value depends on the operation:

    multiplication → 1
    addition       → 0

## Variations

Prefix/suffix information can represent:

- products
- sums
- minimums
- maximums
- counts
- other cumulative state

## Related patterns

- Running State
- Dynamic Programming
- Two Pointers
- Sliding Window
- Prefix Sum