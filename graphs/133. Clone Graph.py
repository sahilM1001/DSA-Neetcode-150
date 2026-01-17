# MEDIUM
# https://leetcode.com/problems/clone-graph/description/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Approach


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : # when node is not valid return None
            return None
        old_new = {} # create map to store old node to new node
        old_new[node] = Node(node.val) # create new node and add it to the map for the first node
        q = deque([node]) # add the first node to queue

        while q:
            # run till q is not empty
            curr = q.popleft() # pop first ele from q
             
            for n in curr.neighbors: 
                # create new nodes for all the neighbors of current node if they are not present in the map
                if n not in old_new:
                    old_new[n] = Node(n.val) # add old neighbor -> new neighbor in map
                    q.append(n) # append the neighbor node to queue
                old_new[curr].neighbors.append(old_new[n]) # add neighbor of current node with latest neighbor from map
            
            
        return old_new[node] # return the pointer to first node in the map
        