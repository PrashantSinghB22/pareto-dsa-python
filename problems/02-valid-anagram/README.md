# Problem 02 — Valid Anagram

## 1. Problem

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

An anagram contains the same characters with the same frequencies, but the characters can appear in a different order.

### Examples

`"anagram"` and `"nagaram"` → `True`

`"rat"` and `"car"` → `False`

---

## 2. Human Logic

Before thinking about Python:

1. Check whether both strings have the same length.
2. Count how many times each character occurs in `s`.
3. Count how many times each character occurs in `t`.
4. Compare the frequencies.
5. If every frequency matches, they are anagrams.
6. Otherwise, they are not.

---

## 3. Key Insight

The order of characters does not matter.

What matters is:

```text
character → frequency