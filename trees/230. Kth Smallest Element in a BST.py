# MEDIUM
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        cur = root
        # iterative dfs approach
        while True:
            while cur:
                # while curr ele, keep appending it to the stack, and move cur to curr.left
                stack.append(cur)
                cur = cur.left
            # when curr no longer valid, pop an element from stack and decrement k by 1
            cur = stack.pop()
            k -= 1

            if k == 0: 
                # if k == 0, return current node as we are at the kth smallest ele in the bst
                return cur.val
            # move cur to curr.right
            # this cur = cur.right can result into None values, and its not an issue, 
            # the code will go ahead and keep popping elements from stack until a valid cur ele is found 
            cur = cur.right