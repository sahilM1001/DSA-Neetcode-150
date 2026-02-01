# MEDIUM
# https://leetcode.com/problems/interleaving-string/description/

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3

# Input: s1 = "", s2 = "", s3 = ""
# Output: true

# Approach

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {} # create dp memo dict
        if len(s1) + len(s2) != len(s3): # if combining s1 and s2 len != s3, we can never create s3 so return false immediately
            return False
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                # if both strings are exhausted return True
                return True
            if (i,j) in memo:
                # if i,j in memo, return that
                return memo[(i,j)]
            # init res, a1, a2 as False
            res, a1, a2= False, False, False
            
            if i < len(s1) and s1[i] == s3[i+j]:
                # if i < len(s1) and char at index i of s1 == char at index i+j of s3,
                # try next char for s1 with same index for s2
                a1 = dfs(i+1, j)

            if j < len(s2) and s2[j] == s3[i+j]:
                # if i < len(s2) and char at index i of s2 == char at index i+j of s3,
                # try next char for s2 with same index for s1
                a2 = dfs(i, j+1)
            res = a1 or a2 # make res true if any a1, or a2 returns true
            memo[(i,j)] = res # update res
            return res # return res

        return dfs(0,0) # start at 0 for s1, 0 for s2  
        