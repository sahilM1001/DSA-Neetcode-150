# MEDIUM
# https://leetcode.com/problems/longest-palindromic-substring/description/

# Given a string s, return the longest palindromic substring in s.

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # for every index in s, we will treat it as a central char, and keep expanding for palindrome strings in left half and right half

            # odd length
            l, r = i, i # for odd length substrings we will init l, r as currrent index

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # while l>=0 and r<len(s) and s[l] == s[r]
                # we calculate the string len, and if it is greater than resLen
                if (r - l + 1) > resLen:
                    resIdx = l # start index as l
                    resLen = r - l + 1 # update resLen to new length
                l -= 1 # decrement l
                r += 1 # increment r

            # even length
            l, r = i, i + 1 # for even length substrings we will init l at i and r at i + 1 ind
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                # while l>=0 and r<len(s) and s[l] == s[r]
                # we calculate the string len, and if it is greater than resLen
                if (r - l + 1) > resLen:
                    resIdx = l # start index as l
                    resLen = r - l + 1  # update resLen to new length
                l -= 1 # decrement l
                r += 1 # increment r

        return s[resIdx : resIdx + resLen] # return string starting at resIdx to resIdx + resLen
        