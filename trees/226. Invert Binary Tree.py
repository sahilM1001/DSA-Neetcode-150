# EASY
# https://leetcode.com/problems/invert-binary-tree/description/

# Given the root of a binary tree, invert the tree, and return its root.

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]


# Approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        # bfs based approach
        q = [] # create empty queue and add root to it if root is not None
        if root is not None:
            q.append(root)
        while q:
            # iterate over the queue and pop from left.
            cur = q.pop(0)
            cur.left, cur.right = cur.right, cur.left # swap left-> right right-> left
            if cur.left: # if current node has left child, add to queue
                q.append(cur.left)
            if cur.right: # if current node has right child, add to queue
                q.append(cur.right)

        return root