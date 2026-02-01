# MEDIUM
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Input: prices = [1]
# Output: 0

# Approach
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for i in range(len(prices)+1)]
        n = len(prices)
        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i+1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i+1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i+2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i+1][False] if i+1 < n else 0
                    dp[i][0] = max(sell, cooldown)
        return dp[0][1]

        
            
        