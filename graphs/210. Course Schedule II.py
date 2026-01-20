# MEDIUM
# https://leetcode.com/problems/course-schedule-ii/description/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Approach
from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a map for each course and its pre requisites. 
        # This will be our adjacency list/matrix for the graph
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = [] # empty output
        visit, cycle = set(), set() # empty visiting and cycle set for marking visited and cycle conditions
        
        def dfs(crs):
            if crs in cycle:
                # if current course is in cycle set, return False
                return False
            if crs in visit:
                # if current course is already visited, return True
                return True

            cycle.add(crs) # add course to cycle so we can prevent adding it in further deeper dfs from its neighbors
            for pre in prereq[crs]:
                # run dfs for all neighbors, when it returns false, return False
                if dfs(pre) == False:
                    return False
            # remove current course from cycle
            cycle.remove(crs)
            visit.add(crs) # add current course to visited
            output.append(crs) # append current course to output sequence
            return True 


        # run dfs for each course and when we get False, return [] 
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        