# MEDIUM
# https://leetcode.com/problems/insert-interval/description/

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

def insert(intervals, newInterval):
    n = len(intervals)
    i = 0
    res = []

    # case when an interval is smaller than the new interval, 
    # we directly append it to the ans arr without any issues, and update i
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    
    # case when an new interval ends after current interval starts,
    # we expand the new interval till this happens and after exiting the loop we add the new interval
    while i < n and newInterval[1] >= intervals[i][0]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    # case when there are any remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1
    return res