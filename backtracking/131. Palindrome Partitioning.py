# MEDIUM
# https://leetcode.com/problems/palindrome-partitioning/description/

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Input: s = "a"
# Output: [["a"]]

# Approach

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # init ans array
        curr = [] # init current ans array
        def backtrack(index):
            if index == len(s):
                res.append(curr.copy())
                return
            for end in range(index, len(s)):
                # create all substrings starting from current index
                sub = s[index: end +1]
                if sub  == sub[::-1]:
                    # if the substring is a partition
                    curr.append(sub) # append it to curr array
                    backtrack(end + 1) # explore recursion path from current index + 1 
                    curr.pop()	# backtrack and pop the last added sub string
        
        backtrack(0) # begin recursion path from 0th index
        return res
        