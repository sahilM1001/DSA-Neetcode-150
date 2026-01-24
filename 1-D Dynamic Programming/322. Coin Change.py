# MEDIUM
# https://leetcode.com/problems/coin-change/description/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Input: coins = [2], amount = 3
# Output: -1

# Input: coins = [1], amount = 0
# Output: 0

# Approach
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount +1) # init dp array of len amount + 1 with each value as amount + 1
        dp[0] = 0 # set dp[0] as 0 as there are 0 ways to create amount 0 with any given coins

        for i in range(1, amount + 1): 
            # for every amount
            for c in coins: 
                # use all coins if i - c >= 0
                if i - c >=0:
                    # update ways for current amount as min between dp[i], 1 + dp[i-c]
                    dp[i] = min(dp[i], 1 + dp[i-c])
        # return dp[amount] if it is less than amount + 1 else -1 as there might be no ways to reach that amount with given change
        return dp[amount] if dp[amount] < amount +1 else -1

        