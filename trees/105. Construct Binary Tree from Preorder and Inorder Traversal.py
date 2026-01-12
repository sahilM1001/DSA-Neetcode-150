# MEDIUM
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        # important things to understand
        # preorder ALWAYS has the node first. But you don't know the size of either branch.
        # inorder ALWAYS has the left branch to the left of the node, and right branch right of the node. So now you know the size of each branch.
        # we use preorder[0] to create root node for the tree
        root = TreeNode(preorder[0])
        stack = [root] # add root node to stack
        inorder_ind = 0 # init inorder_ind as 0
        node = None # init node as None
        for i in preorder[1:]: # loop from preorder index 1 to end
            new_node = TreeNode(i) # create new node with preorder[i] value
            if stack[-1].val != inorder[inorder_ind]:
                # if top of stack.val != inorder[current inorder index], 
                # we are still building left side of the subtree, so we put stack[-1].left = new Node and add new node to the stack
                stack[-1].left = new_node
                stack.append(new_node)
            else:
                # if top of stack.val == inorder[current inorder index]
                while stack and stack[-1].val == inorder[inorder_ind]:
                    # while stack is not empty and top of stack.val == inorder[current inorder index],
                    # we pop from stack and increment inorder index as these are right nodes 
                    node = stack.pop()
                    inorder_ind +=1
                # once the top of stack.val again becomes != inorder[current inorder index] 
                # we make the node.right as new node and append it to the stack
                node.right = new_node
                stack.append(new_node)
        return root
        