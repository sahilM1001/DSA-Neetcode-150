# HARD 
# https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# Approach 1 Brute Force

def trap(height):
    max_water = 0
    for i in range(0, len(height)):
        left = height[0: i]
        left_max = max(left) if len(left) > 0 else 0
        # print("i: ", i)
        # print("left max: ", left_max)
        right = height[i+1 : ]
        right_max = max(right) if len(right) > 0 else 0
        # print("right_max: ", right_max)
        water = min(left_max, right_max) - height[i]
        # print("Water; ", water)
        if water > 0:
            max_water += water
        # print("max_water: ", max_water)
    print("Max water: ", max_water)

height = [4,2,0,3,2,5]
trap(height)

# Approach 2 improving brute force with prefix and suffix array
def trap(height) -> int:
    n = len(height)
    if n == 0:
        return 0

    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i]) # max at each index can be current height or prev height

    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i]) # max at each index can be current height or next height

    res = 0
    for i in range(n):
        res += min(leftMax[i], rightMax[i]) - height[i] # max water at the index will be min(left height, right height) - curr height and add it to res
    return res