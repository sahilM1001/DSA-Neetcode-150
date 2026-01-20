# MEDIUM
# https://neetcode.io/problems/valid-tree/question?list=neetcode150

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# output:
# True
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

# Output:
# false

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Approach
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid graph cannot have edges more than node - 1 and it cannot have a cycle
        if len(edges) > n - 1:
            return False
        
        # create adjacency matrix for undirected graph

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set() # create empty visited set
        def dfs(node, par):
            # if node is already visited, we have encountered a cycle and it is not a valid graph
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n # start dfs from root node and -1 neigbor
        