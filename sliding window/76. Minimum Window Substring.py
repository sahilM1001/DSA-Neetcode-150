# HARD
# https://leetcode.com/problems/minimum-window-substring/description/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Approach 1 - Self written - Failing test cases
def minWindow(s, t):
    l = 0
    r = l + 1 
    str1 = ""
    min_len = float('inf')
    sorted_t_set = sorted(set(t))
    while r < len(s):
        print("L :", l)
        sub = s[l:r+1]
        print("sorted t: ", sorted(set(t)))
        print("sorted sub: ", sorted(set(sub)))
        print("sub: ", sub)
        sorted_sub = sorted(set(sub))
        if all( item in sorted_sub for item in sorted_t_set): 
            print("sub found: ", sub)
            if len(sub) <= min_len:
                str1 = sub
            l+=1
            pass
        else:
            r += 1
    print("STR1: ", str1)
s = "ADOBECODEBANC"
t = "ABC"
minWindow(s,t)

# Approach 2
def minWindow(s, t):
    if t == "":
        return ""
    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1

            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l : r + 1] if resLen != float("infinity") else ""