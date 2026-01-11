# MEDIUM
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        q1 = root
        # we will use the property of a binary search tree
        # in bst, every node's value on the left side of current node will be smaller than current node's value
        # in bst, every node's value on the right side of current node will be greater than current node's value
        
        while q1:
            # while there are items in tree
            if q1.val < p.val and q1.val < q.val:
                # if current.val < p.val and current.val < q.val -> we should look on right side of the tree from now 
                # as every node on the right will be between current.val and max(p.val, q.val) range
                q1 = q1.right
            elif q1.val > p.val and q1.val > q.val:
                # if current.val > p.val and current.val > q.val -> we should look on left side of the tree from now
                # as every node on the left will be between current.val and max(p.val, q.val) range
                q1 = q1.left
            else:
                # if none of the above conditions match, we have found the LCA for our p, q nodes so return that
                return q1   