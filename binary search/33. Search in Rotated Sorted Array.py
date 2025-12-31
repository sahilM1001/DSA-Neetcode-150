# MEDIUM
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

#  Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

def search(nums, target):
    if len(nums) == 1 and nums[0] == target:
        return 0
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[l] <= nums[mid]: # left less than mid val
            if nums[l] <= target < nums[mid]: # left < target < mid -> target is somewhere between l and mid - 1
                r = mid - 1
            else: 
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]: # mid < target <= right target is somewhere between mid + 1 and r
                l = mid + 1
            else:
                r = mid-1

    return -1