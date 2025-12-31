# MEDIUM
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# Approach using sliding window
def characterReplacement(s, k):
    l = 0 
    char_freq = {}
    longest_str = 0
    for r in range(len(s)):
        print("char map: ", char_freq)
        print("char: ", s[r])
        print("r: ", r)
        print("l: ", l)
        if s[r] not in char_freq:
            char_freq[s[r]] = 0
        char_freq[s[r]] += 1

        rep = r - l + 1
        print("mid loop updated char map: ", char_freq)
        print("rep: ", rep)
        if rep - max(char_freq.values()) <= k:
            longest_str = max(longest_str, rep)
            print("updated longest str: ", longest_str)
        else:
            char_freq[s[l]] -= 1
            if not char_freq[s[l]]:
                char_freq.pop(s[l])
            l+=1

    print("longest str: ", longest_str)

s = "AABABBA"
k = 1
characterReplacement(s, k)