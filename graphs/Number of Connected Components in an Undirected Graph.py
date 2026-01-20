# MEDIUM
# https://neetcode.io/problems/count-connected-components/question?list=neetcode150

# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output:
# 2

# Approach
from typing import List
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)] # create adjacency matrix
        visit = [False] * n # init visited array as False 
        for u, v in edges: 
            adj[u].append(v) # create adjancency entry for an edge from u -> v
            adj[v].append(u) # create adjancency entry for an edge from v -> u

        components = 0
        def bfs(node):
            q = deque([node]) # start bfs with passed node
            visit[node] = True # mark current node as visited
            while q:
                cr = q.popleft() # pop from q
                for neig in adj[cr]: 
                    # run loop for all neighbors, if they are not visited already, 
                    # mark them as visited and append to queue
                    if not visit[neig]:
                        visit[neig] = True
                        q.append(neig)

        for node in range(n):
            if not visit[node]: 
                # run bfs for all unvisited nodes in the range of nodes, and update the component count
                bfs(node)
                components += 1
        return components
