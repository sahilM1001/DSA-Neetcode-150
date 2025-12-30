# MEDIUM
# https://leetcode.com/problems/3sum/description/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Approach 1:
def threeSum(nums):
    
    res = []
    for i in range(0, len(nums)):
        hash_set = set()
        for j in range(i+1, len(nums)):
            k = - (nums[i] + nums[j])
            
            if k in hash_set:
                trip = sorted([nums[i], nums[j], k])
                if trip not in res:
                    res.append(trip)
                hash_set.add(nums[j])
            else:
                hash_set.add(nums[j])

nums = [0,0,0]
threeSum(nums)

# Approach 2 

def threeSum(nums):
    res = []
    n = len(nums)
    nums = sorted(nums)
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i-1]: 
            continue
        j = i+1
        k = n - 1
        while j < k:
            ans = nums[i] + nums[j] + nums[k]
            if ans > 0:
                k -= 1
            elif ans < 0:
                j+=1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j+=1
                while j < k and nums[j] == nums[j-1]:
                    j+=1
    return res