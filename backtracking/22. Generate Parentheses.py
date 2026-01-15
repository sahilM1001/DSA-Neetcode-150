# MEDIUM
# https://leetcode.com/problems/generate-parentheses/description/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Approach

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] # init ans array
        curr = [] # init current ans array
        open_count = 0 # track open ( brackets in string
        close_count = 0 # track close ) brackets in string
        def backtrack(open_count, close_count):
            if len(curr) == 2 * n: # a string is valid when it reaches 2 * n size, we use 2 * n as 2 is the number of valid chars in string ( and )
                res.append("".join(curr)) 
                return  # stop recursion
            if open_count < n:
                # if open_count is less than n, we can append one more ( bracket to the string
                curr.append("(") 
                backtrack(open_count +1, close_count) # explore recursion path with current opencount + 1, with unchanged close count
                curr.pop() # backtrack and remove the last added open ( bracket
            if close_count < open_count:
                # if close count is less than open_count, we can append more closing bracket ) to the string and make it valid
                curr.append(")")
                backtrack(open_count, close_count+1) # explore recurion path with unchanged open count and current close_count + 1 
                curr.pop() # backtrack and remove the last added close ) bracket
        backtrack(0, 0) # init backtrack function with both open and close bracket counts as 0
        return res
        