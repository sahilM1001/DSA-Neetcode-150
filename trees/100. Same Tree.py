# EASY
# https://leetcode.com/problems/same-tree/description/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Approach
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        q1 = deque([p]) # init q1 for p tree 
        q2 = deque([q]) # init q2 for q tree
        while q1 and q2:
            # while q1 and q2 are not empty
            for _ in range(len(q1)):
                # run loop till length of q1
                nodeP = q1.popleft() # pop left element from q1
                nodeQ = q2.popleft() # pop left element from q2

                if nodeP is None and nodeQ is None:
                    # if both nodes are null, they are considered equal
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    # if any single node is null, or the values are not same, 
                    # return False as trees are not same
                    return False

                q1.append(nodeP.left) # append left node from current ele of p to q1
                q1.append(nodeP.right) # append right node from current ele of p to q1
                q2.append(nodeQ.left) # append left node from current ele of q to q2
                q2.append(nodeQ.right) # append right node from current ele of q to q2
        return True