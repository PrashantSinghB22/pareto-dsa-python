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
# TESTING
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