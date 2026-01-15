# MEDIUM
# https://leetcode.com/problems/permutations/description/

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Input: nums = [1]
# Output: [[1]]

# Approach
# goal is to generate all permutations of a number array, Permutations != subsets
class Solution:
    def permute(self, nums) :
        self.res = [] # create ans array
        # call external backtrack function with empty perms array, entire nums array, and a boolean array for nums
        self.backtrack([], nums, [False] * len(nums)) 
        return self.res


    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums):
            # if the len of permutation array = len input nums array, we've create a valid permutation 
            # so append it to res and return to stop the recursion
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            # run loop over nums
            if not pick[i]: 
                # if number is not picked up already, 
                # append it to permutation array
                perm.append(nums[i])
                pick[i] = True # mark pick[i] as true to avoid reusing it
                self.backtrack(perm, nums, pick) # call backtracking with new perm with current num, nums array, and modified pick array with current num marked true
                perm.pop() # pop the latest num from perm
                pick[i] = False # make pick i false so the number can be used again in later calls
        