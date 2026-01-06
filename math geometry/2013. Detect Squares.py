# MEDIUM
# https://leetcode.com/problems/detect-squares/description/

# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

# Input
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
# Output
# [null, null, null, null, 1, 0, null, 2]

# Explanation
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // return 1. You can choose:
#                                //   - The first, second, and third points
# detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
# detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
# detectSquares.count([11, 10]); // return 2. You can choose:
#                                //   - The first, second, and third points
#                                //   - The first, third, and fourth points


# Approach
# Key observations about an axis-aligned square:

# All sides are parallel to the x-axis and y-axis
# If (px, py) is one corner and (x, y) is the diagonal opposite corner, then:
# |px - x| == |py - y| (equal side lengths)
# x != px and y != py (otherwise it would not form a square)
# The other two required corners must be:
# (x, py)
# (px, y)
# So the idea is:

# Fix the query point (px, py)
# Try every previously added point (x, y) as a possible diagonal
# If it forms a valid square diagonal, multiply how many times the other two required points exist
# A hash map lets us quickly check how many times a specific point was added.

from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.map = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
    
        self.map[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x,y in self.points:
            if abs(px-x) == abs(py-y) and x != px and y != py:
                res += self.map[(x, py)] * self.map[(px, y)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)