# Frequency Buckets / Bucket Sort

## When to use it

Use this pattern when items have a bounded frequency and we need to
process items according to their frequency.

## Signs to recognize it

- "Top K frequent"
- "Most frequent"
- "Least frequent"
- "Group elements by frequency"
- Frequency is bounded by n

## Core idea

Convert:

number → frequency

into:

frequency → numbers

Example:

1 → 3
2 → 2
3 → 1

becomes:

frequency 3 → [1]
frequency 2 → [2]
frequency 1 → [3]

Then walk from the highest frequency downward.

## Step-by-step logic

1. Count the frequency of every number.
2. Create n + 1 empty buckets.
3. Use each number's frequency as its bucket index.
4. Put the number into that bucket.
5. Start at the highest possible frequency.
6. Walk downward.
7. Add numbers to the result.
8. Stop when k numbers have been collected.

## Template

count frequencies
↓
number → frequency
↓
create buckets
↓
frequency → numbers
↓
walk highest → lowest
↓
collect k

## Common mistakes

- Confusing the number with its frequency.
- Forgetting the `+ 1` when creating buckets.
- Forgetting that multiple numbers can have the same frequency.
- Walking from low frequency to high frequency.
- Forgetting to stop after collecting k elements.
- Using `[[]] * n`, which creates shared list references.

## Variations

- Top K frequent elements
- Bottom K frequent elements
- Frequency-based grouping
- Character-frequency problems

## Related patterns

- Hash Map / Frequency Counting
- Heap / Priority Queue
- Sorting