# MEDIUM
# https://leetcode.com/problems/top-k-frequent-elements/description/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

# Approach 1
from collections import Counter
import heapq
def topKFrequent(nums, k):
        ans = Counter(nums)
        a = ans.most_common(k)
        new1 = []
        for i in range(len(a)):
            new1.append(a[i][0])
        return new1

# Approach 2
from collections import Counter
import heapq
def topKFrequent(nums, k):
        ans = Counter(nums)
        return heapq.nlargest(k, ans.keys(), key=ans.get)