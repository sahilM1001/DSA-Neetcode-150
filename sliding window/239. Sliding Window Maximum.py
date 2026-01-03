# HARD
# https://leetcode.com/problems/sliding-window-maximum/description/

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max in every sliding window.

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Approach 1
# Iterate over the array, create slices of the window size k, find max and append to the output arr
def maxSlidingWindow(nums, k):
    arr = []
    for i in range(0, len(nums) - k +1):
        sub = nums[i:i+k]
        arr.append(max(sub))
    return arr

# Approach 2 
# We want to quickly get the maximum value inside a sliding window that moves across the array.
# A max-heap is perfect for this because it always lets us access the largest element instantly.

# As we slide the window:

# We keep inserting new elements into the heap.
# Some old elements will fall out of the left side of the window.
# If the largest element in the heap is no longer inside the window, we remove it.
# The top of the heap always represents the current maximum for the window.
# This way, we efficiently maintain the maximum even as the window moves.

import heapq
def maxSlidingWindow(nums, k):
    arr = []
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap,(-nums[i], i))
        if i>= k-1:
            while heap[0][1] <= i-k:
                heapq.heappop(heap)
            arr.append(-heap[0][0])
    return arr