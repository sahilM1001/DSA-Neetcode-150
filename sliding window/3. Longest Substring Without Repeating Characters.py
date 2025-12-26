# MEDIUM
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string s, find the length of the longest substring without duplicate characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def lengthOfLongestSubstring(s):
    str_set = set() # Create set for unique adds and faster lookups
    l = 0 # setting left pointer to start of string
    max_so_far = 0 # setting max so far to 0
    for r in range(len(s)): # starting loop at 0, len(s)
        #while current element is in set, remove it and increase left pointer by 1
        while s[r] in str_set: 
            str_set.remove(s[l])
            l+=1
        str_set.add(s[r]) # Add current element to set
        max_so_far = max(max_so_far, len(str_set)) # Update max so far by comparing size of set and previous max
    return max_so_far