# MEDIUM
# https://leetcode.com/problems/word-break/description

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# Approach
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {} # memo dict for memoization
        def dfs(ind):
            if ind == len(s): 
                # if we reach end of word, all previous prefixes/suffixes were valid so return true
                return True
            if ind in memo:
                # reduce recomputation, if we have already explored current index, 
                # it should have a True/False value in the memo dict so return that
                return memo[ind]
            suf = s[ind:] # create suffix from current ind
            for word in wordDict:
                # try every word in the wordDict
                if suf.startswith(word): 
                    # if the suffix startswith a word from the word dict
                    # run dfs at curr index + len(word)
                    if dfs(ind+len(word)):
                        # if the dfs at curr index + len(word) is true, 
                        # we mark memo[index] true and return true 
                        memo[ind] = True
                        return True
            memo[ind]=False # mark memo index False
            return False # return False
        return dfs(0) # start dfs at 0
        