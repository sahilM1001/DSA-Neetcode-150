# MEDIUM
# https://leetcode.com/problems/network-delay-time/description/

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Approach
from collections import defaultdict
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        map_1 = defaultdict(list)
        # creating key, val map of outgoing edges from each node and adding their weights
        for u, v, w in times:
            map_1[u].append([v, w])

        dist = {}
        # initializing distance for each node as inf 
        for i in range(1, n + 1):
            dist[i] = float('inf')

        dist[k] = 0 # starting from node k so marking its distance as 0
        min_heap = [(0, k)] # adding 0, k in the heap
        heapq.heapify(min_heap)

        vis = set() # init vis set

        while min_heap:
            # run loop till heap is not empty

            # pop next smallest time, node from the heap
            ct, c_node = heapq.heappop(min_heap)
            # if node is visited, continue
            if c_node in vis:
                continue
            # if node is not visited, add it to visited set
            vis.add(c_node)
            for nei, w in map_1[c_node]:
                # for all outgoing edges from the node
                if nei not in vis:
                    # if the neighbor is not visited, its new time will be current time + its time
                    new_time = ct + w
                    if new_time < dist[nei]:
                        # if new time is less than old time, we update its time as new time
                        dist[nei] = new_time
                        # add the new_time, neighbor to the heap
                        heapq.heappush(min_heap, (new_time, nei))
        ans = 0
        for i in range(1, n+1):
            # run loop till n+1 nodes to include nth node
            if dist[i] == float('inf'):
                # if any distance is still infinity, return -1
                return -1
            # keep updating ans as max between ans, or current distance
            ans = max(ans, dist[i])
        return ans



        