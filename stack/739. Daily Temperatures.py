# MEDIUM
# https://leetcode.com/problems/daily-temperatures/description/

# Given an array of integers temperatures represents the daily temperatures, return an array answer 
# such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def dailyTemperatures(temperatures):
    if not temperatures: return []
    res = [0] * len(temperatures)
    stack = []
    for index,val in enumerate(temperatures):
        while stack and stack[-1][0] < val:
            stack_top_ind = stack.pop()[1]
            count = index - stack_top_ind
            res[stack_top_ind] = count
        stack.append((val,index))
    return res