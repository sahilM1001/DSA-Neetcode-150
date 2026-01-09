# EASY
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Approach

# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        q = deque([root])
        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth +=1
        return depth
    def diameterOfBinaryTree(self, root) -> int:
        if root is None:
            return 0
        max_dia = float('-inf')
        q = deque([root])
        # bfs based approach
        while q:
            node = q.popleft()
            left_height, right_height = 0, 0
            # for each node in queue, calculate maxDepth for its left subtree, and right subtree. 
            if node.left:
                left_height = self.maxDepth(node.left)
                q.append(node.left)
            if node.right:
                right_height = self.maxDepth(node.right)
                q.append(node.right)
            
            # max diameter of a tree will be its left height + right height,
            # if curr height > max_dia height, update max_dia
            max_dia = max(left_height + right_height, max_dia)

        return max_dia
            
        