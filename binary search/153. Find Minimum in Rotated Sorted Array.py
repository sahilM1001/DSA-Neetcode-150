# MEDIUM
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

# Approach - Binary Search
# whenever an array is sorted but then rotated, it will always have a point where all previous elements are strictly greater than the curr ele, and all next elements will be strictly in increasing order. 
# In this question we have to find such point where elements on both side are greater than curr ele

def findMin(nums) -> int:
    if len(nums) == 1:
        return nums[0]
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid +1 ] < nums[mid]:
            return nums[mid + 1]
        elif nums[mid] < nums[mid-1]:
            return nums[mid]
        elif nums[len(nums)-1] > nums[mid]:
            r = mid 
        else:
            l = mid+1