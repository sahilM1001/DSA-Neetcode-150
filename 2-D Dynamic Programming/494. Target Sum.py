# MEDIUM
# https://leetcode.com/problems/target-sum/description/

# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Input: nums = [1], target = 1
# Output: 1

# Approach
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # create dp memo dict

        def dfs(i, cur_sum):
            if i == len(nums):
                # if we reach end of nums array, and cur sum == target, return 1 else 0
                if cur_sum == target:
                    return 1
                else:
                    return 0
            if (i, cur_sum) in memo:
                # if i, curr sum in memo, return that
                return memo[(i, cur_sum)]
            # explore next index with cur_sum + nums[i] and next index with cur_sum - nums[i]
            res = dfs(i + 1, cur_sum + nums[i]) + dfs(i + 1, cur_sum - nums[i])
            memo[(i,cur_sum)] = res # add res to memo
            return res # return res

        return dfs(0, 0) # start dfs at 0 index, 0 sum
