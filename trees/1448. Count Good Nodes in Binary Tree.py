# MEDIUM
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

# Approach
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root,-float('inf'))) # init q with root node, and max so far as -inf

        while q:
            # pop from q for node and max so far val
            node,maxval = q.popleft() 
            if node.val >= maxval:
                # if current node.value >= max so far, it is a good node
                res += 1

            if node.left:
                # add node.left and max between current node.val or max_val
                # max_val will become current node.val if res was updated above
                q.append((node.left,max(maxval,node.val)))

            if node.right:
                # add node.right and max between current node.val or max_val
                # max_val will become current node.val if res was updated above
                q.append((node.right,max(maxval,node.val)))

        return res
        