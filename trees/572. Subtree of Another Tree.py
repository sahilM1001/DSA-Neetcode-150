# EASY
# https://leetcode.com/problems/subtree-of-another-tree/description/

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root: # a tree cannot be sub root of a null tree so returning false
            return False
        if self.sameTree(root, subRoot):
            # checking if tree is same with root, and sub Root call, if it is same, returning True
            return True
        return (
                self.isSubtree(root.left, subRoot) or #checking if subtree is possible from root.left and subRoot combination 
                self.isSubtree(root.right, subRoot) # chcking if subtree is possible from root.right and subRoot combination
                )
    def sameTree(self, s, t):
        # helper function to check if both trees are same.
        if not s and not t:
            # if both trees are null, return True
            return True
        if s and t and s.val == t.val: 
            # checking if tree1.val == tree2.val
            return (self.sameTree(s.left, t.left) # checking if tree1.left is same as tree2.left
                    and 
                    self.sameTree(s.right, t.right)) # checking if tree1.right is same as tree2.right
        return False
        