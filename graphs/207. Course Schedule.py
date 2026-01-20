# MEDIUM
# https://leetcode.com/problems/course-schedule/description/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Approach
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a map for each course and its pre requisites. 
        # This will be our adjacency list/matrix for the graph
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set() # empty visited set

        def dfs(crs):
            if crs in visiting:
                # if the current course is already visited, and we are revisiting it, 
                # it means there's a cycle in the graph, so we cannot complete all graphs 
                # Cycle detected
                return False
            if preMap[crs] == []:
                # if there are no neighbors for the course, return true
                return True

            visiting.add(crs) # add the course to visited set
            for pre in preMap[crs]:
                # run bfs for all neighbors of the current course
                if not dfs(pre):
                    return False
            visiting.remove(crs) # remove the current course from visited set
            preMap[crs] = [] # mark its neighbors as empty to signify this course was completed
            return True

        # run dfs for each course and when it returns False, return false, else return true finally
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        