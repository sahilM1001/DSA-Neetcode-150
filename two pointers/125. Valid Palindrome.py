# EASY
# https://leetcode.com/problems/valid-palindrome/description/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers
# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Input: s = "race a car"
# Output: false

# Approach

def isPalindrome(s):
    str1 = ""
    for i in range(0, len(s)):
        if s[i].isalnum():
            str1+=s[i].lower()
    str2 = str1[::-1]
    return str1 == str2