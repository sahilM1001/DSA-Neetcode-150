# HARD

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Input: root = []
# Output: []

# Approach
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        result = []
        # serialize using bfs
        while queue: 
            # pop node from left of queue
            node = queue.popleft()

            if node is None:
                # if node is None, append "#" to the result array and continue
                result.append("#")
                continue
            
            result.append(str(node.val)) # when node is not none, we will add str(node.val) to result array
            queue.append(node.left) # append left child to queue 
            queue.append(node.right) # append right child to queue
        return ",".join(result) # return string result 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None
        tokens = data.split(",")
        root = TreeNode(int(tokens.pop(0)))# create root based on first element in tokens array
        q = deque([root])
        while q:
            node = q.popleft() # pop node from queue
            t1 = tokens.pop(0) # pop one ele from left of tokens
            t2 = tokens.pop(0) # pop one ele from left of tokens
            if t1 != "#":
                # if element is not # we create a new node and append it to left of current node, and also add the new node to q
                node.left = TreeNode(int(t1))
                q.append(node.left)
            if t2 != "#":
                # if element is not # we create a new node and append it to right of current node, and also add the new node to q
                node.right = TreeNode(int(t2))
                q.append(node.right)
        return root # finally return root 
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))