# Frequency Counting

## Pattern

Use **Frequency Counting** when you need to know how many times each item occurs.

```text
item → frequency
```

## Recognition Clues

Think Frequency Counting when you see:

* "frequency"
* "number of occurrences"
* "how many times"
* "most/least frequent"
* "same elements with the same counts"
* "same characters"

## Core Idea

```text
Input
 ↓
Count each item
 ↓
Frequency table
 ↓
Compare/use the counts
```

## Algorithm

1. Create a frequency table.
2. Process each item.
3. If unseen → initialize its count.
4. If already present → increment its count.
5. Use the completed frequencies to solve the problem.

## Data Structure Choice

### Dictionary

Use when the possible values are unknown or flexible.

```text
item → count
```

```text
Time:  O(n) average
Space: O(n)
```

### Fixed Array

Use when the possible values belong to a small, fixed domain.

Example:

```text
a-z → 26 positions
```

```text
Time:  O(n)
Space: O(1)
```

## Valid Anagram Variation

Use one frequency table:

```text
s → +1
t → -1
```

If every count ends at `0` → anagram.

## Memory Hook

**"How many times?" → Frequency Counting**

## Common Mistakes

* Checking existence instead of frequency.
* Forgetting to increment counts.
* Using a fixed array without checking constraints.
* Confusing `O(1)` fixed-array space with `O(n)` dictionary space.

## Related Patterns

* Hash Map
* Hash Set
* Sorting
* Fixed-size Array
