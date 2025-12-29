# MEDIUM
# https://leetcode.com/problems/koko-eating-bananas/description/

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Approach 
# minimum K can be 1 and max K can be max(piles), so we will run a binary search between min k to max K, calculate mid point and see if it can complete all piles in less than h hours. If that happens we will update the min(res, mid) and move the right pointer to mid - 1 else move left pointer to mid + 1.

import math

def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r: 
        mid = (l+r)//2
        
        hours = 0
        for i in range(0, len(piles)):
            hours += math.ceil(piles[i] / mid)
        
        if hours <= h:
            res = min(res, mid)
            r = mid-1
        else:
            l = mid+1
    print("res: ", res)
            

piles = [30,11,23,4,20]
h = 5
minEatingSpeed(piles, h)