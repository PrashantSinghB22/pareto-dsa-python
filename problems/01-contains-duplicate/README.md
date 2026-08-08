# Contains Duplicate

## 1. Problem

Given a list of integers, determine whether any value appears more than once.

Return:

* `True` if at least one duplicate exists.
* `False` if every value appears only once.

### Examples

```text
[1, 2, 3, 1] → True
[1, 2, 3, 4] → False
[5, 5]       → True
[1]          → False
[]           → False
```

---

# 2. How to Think About the Problem

The important question is not:

> "How do I compare all these numbers?"

The deeper question is:

> **"How can I determine whether I have seen the current value before?"**

There are multiple ways to answer that question.

We start with the simplest possible solution and then optimize it.

---

# 3. My Initial Idea

My first idea was:

1. Start with the first number.
2. Compare it with all the numbers after it.
3. If a match is found, return `True`.
4. If there is no match, move to the next number.
5. Repeat until all necessary comparisons are complete.
6. If no match is found, return `False`.

This is the **Brute Force** approach.

---

# 4. Brute Force Approach

## 4.1 Human Logic

Imagine solving the problem with paper.

Given:

```text
[5, 3, 8, 2, 5]
```

Start with `5`:

```text
5 vs 3 → different
5 vs 8 → different
5 vs 2 → different
5 vs 5 → match!
```

Once a match is found, we know a duplicate exists.

Therefore:

```text
return True
```

If we reach the end without finding a match:

```text
return False
```

---

## 4.2 Algorithm

1. Start with the first element.
2. Compare it with every element after it.
3. If the two values are equal, return `True`.
4. If no match is found, move to the next element.
5. Repeat the process.
6. If all possible pairs have been checked without a match, return `False`.

---

## 4.3 Brute Force Code

```python
def contains_duplicate_brute(nums):
    for index, num in enumerate(nums):
        for j in range(index + 1, len(nums)):
            if num == nums[j]:
                return True

    return False
```

---

## 4.4 Understanding the Code

### Outer loop

```python
for index, num in enumerate(nums):
```

We need:

* `num` → the current value.
* `index` → the current position.

We need the index because we only want to compare the current value with values **after it**.

---

### Inner loop

```python
for j in range(index + 1, len(nums)):
```

Start at:

```text
index + 1
```

because we don't need to compare a value with itself or with values before it.

Example:

```text
nums = [5, 3, 8, 2, 5]

index = 1
value = 3
```

The values after `3` are at:

```text
indexes 2, 3, 4
```

So:

```python
range(index + 1, len(nums))
```

visits:

```text
2, 3, 4
```

---

### Comparison

```python
if num == nums[j]:
```

This asks:

> Is the current number equal to one of the numbers after it?

If yes, a duplicate exists.

---

### Early return

```python
return True
```

Once we find a duplicate, there is no reason to keep searching.

The answer is already known.

This is called an **early exit**.

---

### Final return

```python
return False
```

If the program reaches this point, every required comparison was completed without finding a duplicate.

Therefore:

```text
No duplicate → False
```

---

# 5. Brute Force Complexity

## Time Complexity

```text
O(n²)
```

Why?

For `n` elements, the number of comparisons is approximately:

```text
(n - 1) + (n - 2) + ... + 2 + 1
```

For example, with 5 elements:

```text
4 + 3 + 2 + 1 = 10 comparisons
```

The exact number is:

```text
n(n - 1) / 2
```

We don't keep the exact formula when describing Big-O.

We care about how the amount of work grows as `n` becomes large.

Therefore:

```text
O(n²)
```

### Intuition

If the input becomes 10× larger, the work can become roughly 100× larger.

That's why quadratic algorithms become expensive for large inputs.

---

## Space Complexity

```text
O(1)
```

We aren't creating a data structure that grows with the input.

We only use a few variables such as:

```text
index
num
j
```

Therefore the extra space is constant.

---

# 6. Why Should We Optimize?

The brute-force solution works.

But notice what it keeps doing:

```text
Compare this number
with many other numbers
```

Then later:

```text
Compare another number
with many other numbers
```

We're repeatedly asking similar questions.

The deeper question is:

> **"Have I already seen this value?"**

If we could remember the values we've encountered, we wouldn't need to compare the current value against every other value.

This leads to the next approach.

---

# 7. Hash Set Approach

## 7.1 Core Insight

Instead of asking:

> "Which other numbers equal this number?"

we ask:

> **"Have I seen this number before?"**

We can keep track of previously encountered values.

For example:

```text
Input:

[5, 3, 8, 2, 5]
```

Walk through it:

```text
Seen = {}

See 5
→ 5 not seen
→ remember 5

Seen = {5}

See 3
→ 3 not seen
→ remember 3

Seen = {5, 3}

See 8
→ 8 not seen
→ remember 8

Seen = {5, 3, 8}

See 2
→ 2 not seen
→ remember 2

Seen = {5, 3, 8, 2}

See 5
→ 5 already seen
→ duplicate!
→ True
```

---

# 8. Why Use a Set?

We need a data structure that is good at answering:

> "Does this value already exist?"

A Python `set` is designed for membership checking.

Example:

```python
seen = set()
```

Then:

```python
num in seen
```

asks:

> "Is `num` already inside the set?"

Set membership is **O(1) on average**.

That allows us to avoid scanning through previously seen values.

---

# 9. Hash Set Algorithm

1. Create an empty set called `seen`.
2. Iterate through every number in `nums`.
3. Check whether the current number already exists in `seen`.
4. If it exists, return `True`.
5. Otherwise, add the number to `seen`.
6. If the entire list is processed without finding a duplicate, return `False`.

---

# 10. Hash Set Code

```python
def contains_duplicate_hashset(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
```

---

# 11. Understanding the Code

## Create the set

```python
seen = set()
```

Initially:

```text
seen = {}
```

Conceptually, it is an empty collection.

Its purpose is:

> Store values that we've already encountered.

---

## Process each number

```python
for num in nums:
```

We visit each value exactly once.

---

## Check membership

```python
if num in seen:
```

This asks:

> Have I already encountered this value?

If yes:

```python
return True
```

because we've found a duplicate.

---

## Remember the value

```python
seen.add(num)
```

If the number wasn't already present, store it.

Then we'll be able to recognize it if it appears again later.

---

## No duplicate

```python
return False
```

If the entire list is processed without finding a repeated value, there are no duplicates.

---

# 12. Hash Set Complexity

## Time

```text
O(n) average
```

Why?

We process each element once.

For each element, we perform set membership checking, which is `O(1)` on average.

Therefore:

```text
n elements × O(1)
=
O(n)
```

---

## Space

```text
O(n)
```

In the worst case, every element is unique.

For example:

```text
[1, 2, 3, 4, 5, 6, ...]
```

The set needs to remember all of them.

Therefore the additional memory can grow with `n`.

---

# 13. Final Approach Comparison

| Approach    |         Time | Space | Core Idea                       |
| ----------- | -----------: | ----: | ------------------------------- |
| Brute Force |        O(n²) |  O(1) | Compare every pair              |
| Hash Set    | O(n) average |  O(n) | Remember previously seen values |

---

# 14. The Optimization Pattern

The important transformation was:

```text
Brute Force:

Compare current value
against many other values
```

↓

```text
Optimization:

Remember previously seen values
```

↓

```text
Hash Set:

Ask "Have I seen this before?"
```

This is an example of:

> **Trading space for time.**

We use additional memory to reduce repeated computation.

---

# 15. Pattern Recognition

## Pattern Name

**Hash Set / Membership Checking**

---

## When to Use It

Consider a set when the problem asks you to determine things like:

```text
Have I seen this before?

Does this value already exist?

Are there duplicates?

Is this element unique?

Have I encountered this item previously?
```

---

## Recognition Clues

Watch for phrases such as:

```text
"contains duplicates"

"appears more than once"

"already seen"

"check whether an element exists"

"find repeated values"

"determine if two values are the same"
```

These clues should make you consider:

```text
Hash Set
```

---

## Core Idea

Maintain a collection of values that have already been processed.

For every new value:

```text
Is it already stored?
     │
   YES → duplicate / match found
     │
    NO → store it
```

---

# 16. Memory Hook

Imagine entering a building where every person gets checked at the door.

The security guard keeps a list of people who have already entered.

When someone arrives:

```text
Have I seen this person?

YES → Something is repeated.

NO → Add them to the list.
```

A Hash Set works similarly:

```text
Person arrives
    ↓
Have I seen them?
    ↓
YES → duplicate
NO  → remember them
```

### Memory sentence

> **"If the problem asks 'Have I seen this before?', think Hash Set."**

---

# 17. Important Python Concepts Learned

## `enumerate()`

Used when we need both:

```text
index + value
```

Example:

```python
for index, num in enumerate(nums):
```

---

## `range()`

Useful when we need to control which indexes we visit.

Example:

```python
range(index + 1, len(nums))
```

means:

> Start after the current index and continue to the end.

---

## `set`

A collection designed for unique values and efficient membership checking.

```python
seen = set()
```

---

## `in`

Used to check membership:

```python
if num in seen:
```

---

## `.add()`

Adds an element to a set:

```python
seen.add(num)
```

---

## `return`

Ends the function and sends a result back.

```python
return True
```

---

# 18. Dry Run — Brute Force

Input:

```text
[5, 3, 8, 2, 5]
```

Start with:

```text
5
```

Compare:

```text
5 vs 3 → no
5 vs 8 → no
5 vs 2 → no
5 vs 5 → YES
```

Return:

```text
True
```

---

# 19. Dry Run — Hash Set

Input:

```text
[5, 3, 8, 2, 5]
```

| Current | Seen Before | Action        |
| ------: | ----------- | ------------- |
|       5 | No          | Add 5         |
|       3 | No          | Add 3         |
|       8 | No          | Add 8         |
|       2 | No          | Add 2         |
|       5 | **Yes**     | Return `True` |

Final answer:

```text
True
```

---

# 20. Edge Cases

## Empty list

```text
[]
```

No values exist, so there cannot be a duplicate.

```text
False
```

---

## One element

```text
[5]
```

A single value cannot appear twice.

```text
False
```

---

## Two identical values

```text
[5, 5]
```

The second `5` is already known.

```text
True
```

---

## Negative numbers

```text
[-1, -2, -1]
```

The logic doesn't change.

```text
True
```

---

## All values unique

```text
[1, 2, 3, 4, 5]
```

No value is encountered twice.

```text
False
```

---

# 21. Common Beginner Mistakes

### Mistake 1 — Using `append()` on a set

Incorrect:

```python
seen.append(num)
```

`append()` belongs to lists.

For sets:

```python
seen.add(num)
```

---

### Mistake 2 — Returning `False` when a duplicate is found

Incorrect reasoning:

```text
Already seen → False
```

The problem asks:

> "Does a duplicate exist?"

Therefore:

```text
Duplicate found → True
No duplicate → False
```

---

### Mistake 3 — Returning inside the loop too early

This:

```python
for num in nums:
    return ...
```

stops after the first iteration.

A loop should continue unless we've actually found the final answer.

---

### Mistake 4 — Confusing index and value

Given:

```text
[5, 3, 8]
```

the indexes are:

```text
0, 1, 2
```

The values are:

```text
5, 3, 8
```

`enumerate()` gives both.

---

### Mistake 5 — Assuming every problem needs nested loops

Nested loops are sometimes necessary, but they should make you ask:

> "Am I repeatedly searching for information that I could remember instead?"

---

# 22. My Learning Mistake

My initial approach was to compare every number with the numbers after it.

That works, but it repeats a lot of comparisons.

The important realization was:

> I don't actually need to compare every pair. I only need to know whether the current value has already appeared.

That led to the Hash Set approach.

---

# 23. Key Lesson

The biggest lesson from this problem isn't actually `set()`.

It's this:

> **Optimization often comes from identifying information that your algorithm keeps rediscovering and finding a way to remember it.**

Brute Force:

```text
Repeatedly search
```

Optimized:

```text
Remember previous information
```

This idea appears throughout DSA.

---

# 24. Related Patterns

This problem connects to:

* Hash Map
* Frequency Counting
* Two Sum
* Sliding Window
* Unique Element Problems
* Membership Checking

The Hash Set pattern should be considered whenever we need fast membership testing.

---

# 25. Retrieval Questions

Do not look at the solution when answering these.

### Basic

1. What problem are we solving?
2. What does the function return?
3. Why does the brute-force solution use two loops?
4. Why do we start the inner loop at `index + 1`?

### Complexity

5. Why is brute force `O(n²)`?
6. Why is the Hash Set approach `O(n)` average time?
7. Why does the Hash Set approach use `O(n)` space?

### Data Structures

8. Why did we choose a set?
9. Why wouldn't a normal list give us the same average membership performance?
10. What is the purpose of `seen`?

### Pattern Recognition

11. What phrase in a problem should make you think:

```text
"Have I seen this before?"
```

12. What data structure should you consider when you need efficient membership checking?

### Deeper Understanding

13. What exactly are we trading when moving from brute force to Hash Set?

14. If extra memory were forbidden, which approach would become more attractive?

15. Why is the Hash Set approach considered optimal for the usual constraints of this problem?

---

# 26. One-Sentence Summary

> **When I need to know whether I've encountered a value before, I can store previously seen values in a Hash Set and perform fast membership checks.**

---

# 27. Pattern Card

```text
Pattern Name:
Hash Set / Membership Checking

When to use:
When we need to quickly determine whether a value
has already been encountered.

Recognition clues:
"duplicate"
"already seen"
"appears more than once"
"contains"
"exists"
"unique"

Core idea:
Store previously encountered values.

Step-by-step:
1. Create an empty set.
2. Process each value.
3. Check whether it already exists.
4. If yes, handle the duplicate/match.
5. If no, add it.
6. Continue.

Typical complexity:
O(n) average time
O(n) space

Memory Hook:
"Have I seen this before?" → Hash Set

Related patterns:
Hash Map
Frequency Counting
Sliding Window
Two Sum
Membership Checking
```

---

# 28. Final Code

```python
# ==========================================
# 1. BRUTE FORCE
# Time: O(n²)
# Space: O(1)
# ==========================================

def contains_duplicate_brute(nums):
    for index, num in enumerate(nums):
        for j in range(index + 1, len(nums)):
            if num == nums[j]:
                return True

    return False


# ==========================================
# 2. HASH SET — OPTIMAL
# Time: O(n) average
# Space: O(n)
# ==========================================

def contains_duplicate_hashset(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    [5, 3, 8, 2, 5],
    [1, 2, 3, 4],
    [5, 5],
    [1],
    []
]

for nums in test_cases:
    print(f"Input: {nums}")
    print(f"Brute Force: {contains_duplicate_brute(nums)}")
    print(f"Hash Set:    {contains_duplicate_hashset(nums)}")
    print()
```

---

# 29. Status

```text
Problem: Contains Duplicate

Brute Force:
✓ Understood
✓ Implemented
✓ Tested
✓ Complexity understood

Hash Set:
✓ Understood
✓ Implemented
✓ Tested
✓ Complexity understood

Pattern:
✓ Hash Set / Membership Checking

Next:
→ Retrieval practice
→ Add problem to tracker
→ Record mistakes
→ Git commit
→ Review scheduling
→ Move to next problem
```
