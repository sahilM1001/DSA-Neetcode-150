# MEDIUM
# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Approach
from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        ans = []
        q = deque([root]) # init q with root
        while q:
            last_node = None
            level_size = len(q) # calculate len of q
            for i in range(level_size):
                # iterate the q, pop its left, and append its child
                node = q.popleft()
                last_node = node.val # keep updating last_node with node.val in each iteration
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # at exit of loop, last node will be the node which is visible from right side view of the tree,
            # so we append that
            ans.append(last_node)
            
        return ans

        
