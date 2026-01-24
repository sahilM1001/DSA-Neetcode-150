# MEDIUM
# https://leetcode.com/problems/palindromic-substrings/description/

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Approach

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 # init count as 0

        for i in range(len(s)):
            # for every index in s, we will treat it as a central char, and keep expanding for palindrome strings in left half and right half

            # odd length
            l, r = i, i # for odd length substrings we will init l, r as currrent index
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # while l>=0 and r<len(s) and s[l] == s[r] keep incrementing palindrome string count
                count +=1
                l -= 1 # decrement l
                r += 1 # increment r

            # even length
            l, r = i, i + 1 # for even length substrings we will init l at i and r at i + 1 ind
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # while l>=0 and r<len(s) and s[l] == s[r] keep incrementing palindrome string count
                count +=1
                l -= 1 # decrement l
                r += 1 # increment r

        return count # count of palindromic substrings in the given string
        