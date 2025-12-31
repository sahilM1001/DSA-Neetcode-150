# MEDIUM
# https://leetcode.com/problems/permutation-in-string/description/

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 
def checkInclusion(s1, s2):
    s1_len = len(s1)
    s1 = sorted(s1)
    print("s1: ", s1)
    for i in range(0, len(s2)-len(s1) + 1):
        sub = sorted(s2[i:i+s1_len])
        print(sub)
        if sub == s1:
            print(f"found sub: {sub} == s1 {s1}")
            break

s1 = "adc"
s2 = "dcda"
checkInclusion(s1, s2)