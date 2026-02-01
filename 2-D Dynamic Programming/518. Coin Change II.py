# MEDIUM
# https://leetcode.com/problems/coin-change-ii/description/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Input: amount = 10, coins = [10]
# Output: 1

# Approach
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {} # create dp memo dict
        def dfs(i, rem_amount):
            if rem_amount == 0:
                return 1 # if we exhaust all amount, return 1
            if i == len(coins) and rem_amount > 0:
                return 0 # if we complete all coins but still amount is left return 0
            if (i, rem_amount) in memo: 
                # if index, amount in memo, return 
                return memo[(i, rem_amount)]
            if coins[i] > rem_amount:
                # if current coin greater than remaining amount, try next coin
                res =  dfs(i+1, rem_amount)
            if coins[i] <= rem_amount:
                # if current coint less than remaining amount, try current coin as well as next coin
                res = dfs(i, rem_amount-coins[i]) + dfs(i + 1, rem_amount)
            
            memo[(i, rem_amount)] = res # update index, remaining amount to res
            return res # return res
        return dfs(0, amount) # start dfs at index 0 with remaining_amount = amount
