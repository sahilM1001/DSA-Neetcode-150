# MEDIUM
# https://leetcode.com/problems/product-of-array-except-self/description/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Naive Solution
def productExceptSelf_naive(nums):
    ans = []
    prod = 1
    for i in range(len(nums)):
        prod *= nums[i]
    for i in range(len(nums)):
        ans.append(prod // nums[i])
    print("ANS: ", ans)


# Approach Sahil

def productExceptSelf_Sahil(nums):
    print("INPUT: ", nums)
    prefix = [1]*len(nums)
    postfix = [1]*len(nums)

    for i in range(0, len(nums)):
        if i -1 <= 0 :
            prefix[i] = 1 * nums[i]
        else:
            prefix[i] = prefix[i-1] * nums[i]

    print("PREFIX: ", prefix)
    for i in range(len(nums)-1,-1,-1):
        if i + 1 >= len(nums):
            postfix[i] = postfix[i] * nums[i]
        else:
            postfix[i] = postfix[i+1] * nums[i]
    print("POSTFIX: ", postfix)
    ans = []
    for i in range(0, len(nums)):
        prod = 0
        if i == 0:
            prod = prefix[i] * postfix[i+1]
        elif i == len(nums)-1:
            prod = postfix[i] * prefix[i-1]
        else: 
            prod = prefix[i-1] * postfix[i + 1]
        ans.append(prod)
    print("ANS: ", ans)


# Approach Neetcode 
def productExceptSelf(nums):
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    #reverse array iteration
    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    print("RESULT: ", result)

nums = [-1,1,0,-3,3]
productExceptSelf_Sahil(nums)