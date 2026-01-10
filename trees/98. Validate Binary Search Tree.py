# MEDIUM
# https://leetcode.com/problems/validate-binary-search-tree/description/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: root = [2,1,3]
# Output: true


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Approach
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True
         # init deque with root and left bound as - inf and right bound as +inf
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            # pop from left for every iteration
            node, left, right = q.popleft()
            # if node's val is not between left max and right min, it is an invalid binary search tree
            if not (left < node.val < right):
                return False
            if node.left:
                # append curr node's left, make the left bound as curr left max, and right bound as current node's val
                q.append((node.left, left, node.val))
            if node.right:
                # append curr node's right, make the left bound as current node's val and right bound as curr right min
                q.append((node.right, node.val, right))

        return True
        