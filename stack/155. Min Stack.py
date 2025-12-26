# MEDIUM
# https://leetcode.com/problems/min-stack/description/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.stack = [] # init normal stack
        self.min_stack = [] # init min stack to store min vals
        

    def push(self, val: int) -> None:
        self.stack.append(val) # append val to stack
        if self.min_stack:
            val = min(self.min_stack[-1], val) # update min val by comparing min stack top and current val
        self.min_stack.append(val) # add updated val to min stack, it can have duplicates
        

    def pop(self) -> None:
        self.stack.pop() # pop from normal stack
        self.min_stack.pop() # pop from min stack 
        

    def top(self) -> int:
        return self.stack[-1] # returns top ele

    def getMin(self) -> int:
        return self.min_stack[-1] # returns min ele from min stack