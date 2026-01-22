# MEDIUM
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

# Approach
import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        vis = [False] * len(points)
        vis[0] = True

        min_heap = []
        total_cost = 0
        connected = 1  # number of points in MST

        # initialize heap using starting node (0)
        for j in range(1, len(points)):
            dist = abs(points[0][0] - points[j][0]) + abs(points[0][1] - points[j][1])
            heapq.heappush(min_heap, (dist, j))

        while connected < len(points):
            cost, next_point = heapq.heappop(min_heap)

            if vis[next_point]:
                continue

            # add this point to MST
            vis[next_point] = True
            total_cost += cost
            connected += 1
             # update heap using the newly added point
            for j in range(len(points)):
                if not vis[j]:
                    new_dist = abs(points[next_point][0] - points[j][0]) + abs(points[next_point][1] - points[j][1])
                    heapq.heappush(min_heap, (new_dist, j))
        return total_cost