# MEDIUM
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s > target:
                # reduce r to find smaller number as input array is sorted, r - 1 will be smaller than r, keep l same 
                r -=1
            else:
                # increase l to find bigger number as input array is sorted, l + 1 will be bigger than l, keep r same 
                l +=1