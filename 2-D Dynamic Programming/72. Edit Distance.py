# MEDIUM
# https://leetcode.com/problems/edit-distance/description/

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')


# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

# Approach
# solved using levenshtein distance, which helps in finding min operations required to make string equal

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} # create dp memo dict

        def dfs(i, j):
            if  i == 0:
                # if we reach end of word 1, return j index
                return j
            if j == 0:
                # if we reach end of word 2 return i index
                return i
            if (i,j) in memo:
                # if i,j in memo, return 
                return memo[(i,j)]
            if word1[i-1] == word2[j-1]:
                # if prev char in word1 == prev char word2, decrement both index and run dfs again wth i-1, and j-1
                res = dfs(i-1, j-1)
            else:
                # try inserting by decrementing j index and keeping i index same
                insert = dfs(i, j-1)
                # try deleting by decrementing i index and keeping j index same
                delete = dfs(i-1, j)
                # try replacing by decrementing both indexes
                replace = dfs(i-1, j-1)
                # update res to 1 + minimum cost between insert, delete and replace
                res = 1 + min(insert, delete, replace)
            memo[(i,j)] = res # update memo i,j with res 
            return res # return res
        return dfs(len(word1), len(word2)) # start dfs at end of both words
        
