# Canonical Signature + Hash Map

## When to use it

When different inputs should be grouped together because they share the same normalized representation.

## Signs to recognize it

- Need to group equivalent objects.
- Order doesn't matter.
- Different inputs can produce the same signature.
- Need fast lookup of an existing group.

## Core idea

    object
       ↓
    signature
       ↓
    Hash Map key
       ↓
    group

Example:

    "eat" → "aet" → group
    "tea" → "aet" → same group

## Common signatures

- Sorted characters
- Frequency counts
- Normalized strings
- Other canonical representations

## Complexity

Depends on how the signature is created.

## Common mistakes

- Choosing a signature that doesn't uniquely represent the property.
- Forgetting that dictionary keys must be hashable.
- Using a mutable list as a key.

## Related patterns

- Frequency Counting
- Hash Map / Lookup
- Sorting