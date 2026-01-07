# MEDIUM
# https://leetcode.com/problems/merge-intervals/description/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.

# Approach

def merge(intervals):

    # sort the intervals based on start time
    sorted_intervals = sorted(intervals,key= lambda x: x[0])
    new_arr = []
    for interval in sorted_intervals:
        # if current interval starts after the last interval's end time in the ans arr, 
        # just append as they are non overlapping
        if not new_arr or interval[0] > new_arr[-1][1]:
            new_arr.append(interval)
        else:
            # if current interval starts before last interval's end time, 
            # merge the intervals by updating end time of the last interval in ans arr with 
            # max of current interval's endtime and ans array's last interval's end time
            new_arr[-1][1] = max(interval[1], new_arr[-1][1])
    return new_arr