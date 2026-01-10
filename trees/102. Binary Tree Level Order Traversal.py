# MEDIUM
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Input: root = [1]
# Output: [[1]]

# Approach
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        # init queue with root element
        q = deque([root])
        ans = []
        while q: 
            # for every q ele
            a = []
            for i in range(len(q)):
                # run till length of q, so for root this loop will run once, then next time it will run 2 times, 
                # as root.left and root.right will be added to the queue on root's run
                node = q.popleft()
                # pop element from q's left and append it to array
                a.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # append array to ans array
            ans.append(a)
        return ans
        
            
        