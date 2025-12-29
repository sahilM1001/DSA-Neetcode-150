# MEDIUM
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4

# Approach 1: Brute Force

def longestConsecutive(nums):
    
    max_len = 0

    for i in range(0, len(nums)):
        curr = nums[i]
        length = 1
        while curr + 1 in nums:
            length+=1
            curr +=1
        max_len = max(max_len, length)
    print("MAX LEN: ", max_len) 

nums = [1,0,1,2]
longestConsecutive(nums)

# Approach 2: Using sorting
# We first sort the input array, then iterate over it, 
# if curr num - 1 == last_small, increase count and last_small = curr_num
# if last_small != curr_num, count = 1 start new seq, last_small = curr_num
# longest_seq = max(longest_seq, count)
#  
def longestConsecutive_optimal(nums):
    max_len = 0
    count = 1
    last_small = float('-inf')
    nums.sort()
    for i in range(0, len(nums)):
        curr = nums[i]
        if curr - 1 == last_small:
            count+=1
            last_small = curr
        if last_small != curr:
            count = 1
            last_small = curr
        max_len = max(max_len, count)
    print("MAX LEN: ", max_len) 

nums = [1,0,1,2]
longestConsecutive_optimal(nums)
