# ============================================================
# Problem 04 — Best Time to Buy and Sell Stock
# ============================================================
#
# Given an array of stock prices, choose one day to buy and a
# later day to sell. Return the maximum possible profit.
#
# You may make only ONE transaction.
#
# If no profit is possible, return 0.
#
# Examples:
#
# [7, 1, 5, 3, 6, 4] -> 5
# [7, 6, 4, 3, 1]    -> 0
#
# Important constraint:
#
# BUY must happen before SELL.
#
# ============================================================


# ============================================================
# Solution 1 — Brute Force
# ============================================================
#
# Idea:
#
# Try every possible buy/sell pair.
#
# For each buy index i, check every later sell index j.
#
# Calculate:
#
#     profit = prices[j] - prices[i]
#
# Keep the largest profit found.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#
# ============================================================

def max_profit_brute(prices):

    best_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):

            profit = prices[j] - prices[i]

            if profit > best_profit:
                best_profit = profit

    return best_profit


# ============================================================
# Solution 2 — Track Minimum Price ⭐ Optimal
# ============================================================
#
# Idea:
#
# We don't need to compare every possible pair.
#
# For each day, ask:
#
#     "If I sell today, what is the best profit I could make?"
#
# To answer that, we only need the cheapest price seen before.
#
# Keep track of:
#
#     minimum_price -> cheapest price seen so far
#     best_profit   -> maximum profit found so far
#
# For every price:
#
#     profit = price - minimum_price
#
# Then update best_profit if necessary.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# ============================================================

def max_profit(prices):

    minimum_price = prices[0]
    best_profit = 0

    for price in prices:

        if price < minimum_price:
            minimum_price = price

        profit = price - minimum_price

        if profit > best_profit:
            best_profit = profit

    return best_profit


# ============================================================
# Key Insight
# ============================================================
#
# We don't need every previous price.
#
# When selling today, only the CHEAPEST previous price matters.
#
#     current price - cheapest previous price
#                    ↓
#               possible profit
#
# Then compare that profit with best_profit.
#
# This reduces the problem from checking every pair to making
# one pass through the array.
#
# Memory Hook:
#
#     "Buy at the cheapest price seen so far,
#      then ask what profit today's price gives me."
#
# ============================================================


# ============================================================
# Pattern
# ============================================================
#
# Pattern: Track the Best State So Far
#
# Recognition clues:
#
# - Process an array from left to right.
# - A previous value affects the current decision.
# - Only the BEST previous value matters.
# - We can maintain a small amount of state instead of
#   comparing every pair.
#
# Core idea:
#
#     Maintain the best useful information seen so far.
#
# Here:
#
#     minimum_price
#     best_profit
#
# ============================================================


# ============================================================
# Tests
# ============================================================

test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2, 3, 4, 5], 4),
    ([5, 4, 3, 2, 1], 0),
    ([2, 4, 1, 7], 6),
]


print("Testing Best Time to Buy and Sell Stock...\n")

for prices, expected in test_cases:

    brute_result = max_profit_brute(prices)
    optimal_result = max_profit(prices)

    print(f"prices={prices}")
    print(f"  Brute:   {brute_result}")
    print(f"  Optimal: {optimal_result}")
    print(f"  Expected: {expected}")

    assert brute_result == expected
    assert optimal_result == expected

    print("  ✓ All solutions passed\n")


print("All tests passed!")