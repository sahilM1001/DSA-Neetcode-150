# EASY
# https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

def isValid(s):
    stack = []
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            peek = stack[-1]
            if (peek == '(' and char == ')') or (peek == '[' and char == ']') or (peek == '{' and char == '}'):
                stack.pop()
            else:
                return False
    return len(stack) == 0