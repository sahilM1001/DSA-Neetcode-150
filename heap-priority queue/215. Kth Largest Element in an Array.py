# MEDIUM
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Approach
# Create a max heap, then iterate till k-1 and return top of heap

import heapq
def findKthLargest(nums, k):
    heap = [-x for x in nums]
    heapq.heapify(heap)
    
    for i in range(0, k-1):
        heapq.heappop(heap)
        
    return -heap[0]
    