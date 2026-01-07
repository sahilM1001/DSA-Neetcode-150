# MEDIUM
# https://leetcode.com/problems/non-overlapping-intervals/description/

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Approach

def eraseOverlapIntervals(intervals):
    # sort intervals based on start time
    sorted_intervals = sorted(intervals,key= lambda x: x[0])
    ans = 0 
    prevEnd = sorted_intervals[0][1] # init prevEnd with first interval's end time

    # iterate loop from index 1
    for start, end in sorted_intervals[1:]:
        if start >= prevEnd: # if current start > prevEnd, update prevEnd to current end
            prevEnd = end
        else:
            # current start < prevEnd meaning there is an overlap
            ans +=1
            prevEnd = min(end, prevEnd) # update prevEnd with min val between current end and prevEnd
    return ans