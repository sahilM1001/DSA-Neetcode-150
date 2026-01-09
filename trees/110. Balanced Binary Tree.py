# EASY
# https://leetcode.com/problems/balanced-binary-tree/description/

# Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        stack = []
        node = root
        last = None
        depths = {}
        # iterative dfs based approach

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False

                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right

        return True
        