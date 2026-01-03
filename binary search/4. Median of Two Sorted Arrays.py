# HARD
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Approach - 1
def findMedianSortedArrays(nums1, nums2):
    newList= nums1 + nums2 # create new list
    newList.sort() # sort new list
    #print(newList)
    leng = len(newList) # get length
    if leng % 2 == 0: # if len is even then median is (len//2 + len//2-1) /  2
        return float(newList[leng//2] + newList[leng//2-1])/2
    else: # if len is odd median is len // 2
        return float(newList[leng//2])
    
# Approach 2
from statistics import median

def findMedianSortedArrays(nums1, nums2):
    return median(sorted(nums1 + nums2))