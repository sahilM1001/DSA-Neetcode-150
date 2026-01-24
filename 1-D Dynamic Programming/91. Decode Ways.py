# MEDIUM
# https://leetcode.com/problems/decode-ways/description/

# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

# "1" -> 'A'

# "2" -> 'B'

# ...

# "25" -> 'Y'

# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:

# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Input: s = "12"

# Output: 2

# Explanation:

# "12" could be decoded as "AB" (1 2) or "L" (12).

# Input: s = "226"

# Output: 3

# Explanation:

# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Approach

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1} # to decode final string there is one way at the start so we init that

        def dfs(i):
            if i in dp:
                # at any point, if we reach a string which is already explored previously and in dp, we can return its ways
                return dp[i] 
            if s[i] == '0':
                # if current char is 0 we return 0 
                return 0

            res = dfs(i + 1) # call dfs for next char in string
            if i < len(s) - 1:
                # if ind is less than string end - 1, meaning there are two chars remaining in the string
                # we explore if it is a valid two digit number, and call dfs for i+2 
                if (s[i] == '1' or
                   (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2)
                dp[i] = res # update ways for current index to res
            return res # return res

        return dfs(0) # start dp at 0 index
        