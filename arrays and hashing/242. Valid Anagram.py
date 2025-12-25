# EASY
# https://leetcode.com/problems/valid-anagram/description/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Input: s = "anagram", t = "nagaram"

# Output: true

# Input: s = "rat", t = "car"

# Output: false

# Approach 1

def isAnagram(s, t) :
    if len(s) != len(t):
        return False
    freqs = [0] * 26
    for i in s:
        freqs[ord(i) - 97] +=1
    for i in t:
        if freqs[ord(i)-97] > 0:
            freqs[ord(i)-97] -= 1
    return True if sum(freqs) == 0 else False

# Approach 2

def isAnagra(s, t):
    return sorted(s) == sorted(t)