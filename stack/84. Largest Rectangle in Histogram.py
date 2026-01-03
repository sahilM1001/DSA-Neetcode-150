# HARD
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Approach
# For each bar, we want to know how far it can stretch left and right before bumping into a shorter bar.
# That distance tells us the widest rectangle where this bar is the limiting height.
# To efficiently find the nearest smaller bar on both sides, we use a monotonic stack that keeps indices of bars in increasing height order.
# This lets us compute boundaries in linear time instead of checking outward for every bar.
def largestRectangleArea(heights) -> int:
    n = len(heights)
    stack = []

    leftMost = [-1] * n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftMost[i] = stack[-1]
        stack.append(i)

    stack = []
    rightMost = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            rightMost[i] = stack[-1]
        stack.append(i)

    maxArea = 0
    for i in range(n):
        leftMost[i] += 1
        rightMost[i] -= 1
        maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
    return maxArea