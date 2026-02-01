# HARD
# https://leetcode.com/problems/distinct-subsequences/description/

# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

# Approach

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # if t > s, there cannot be any subsequences in s that result in t so we return 0
        if len(t) > len(s):
            return 0
        t_len = len(t) # len of t
        s_len = len(s) # len of s
        memo = {} # create dp memo dict
        def dp(i,j):
            if j == t_len:
                # if we exhaust t return 1
                return 1
            if i == s_len and j < t_len:
                # if we exhaust s and j < length of t the subsequence cannot be formed so return 0
                return 0
            if (i,j) in memo:
                # if i, j in memo, return 
                return memo[(i,j)]
            res = dp(i + 1, j) # explore next index in s with current index in t
            if s[i] == t[j]:
                # if char at index i in s == char at index j in s
                # explore next index in bot s, and t with i+1 and j+1
                # and add ans to res
                res += dp(i + 1, j + 1)
            memo[(i, j)] = res # update res
            return res # return res
        return dp(0,0) # start dp with 0,0 index for both s and t
        