# HARD
# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/


# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] 
# describes the ith interval starting at lefti and ending at righti (inclusive). 
# The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

# You are also given an integer array queries. 
# The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. 
# If no such interval exists, the answer is -1.

# Return an array containing the answers to the queries.

# Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# Output: [3,3,1,4]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
# - Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
# - Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
# - Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.


# Approach

import heapq


def minInterval(intervals, queries):
        ans = []
        intervals = [[r-l +1, l, r] for l, r in intervals]
        heapq.heapify(intervals)
        for q in queries:
            temp = []
            found = False
            while intervals:
                dist, l,r = heapq.heappop(intervals)
                if q in range(l, r+1):
                    print(f"found for :{q} < [{l}, {r}]")
                    ans.append(dist)
                    heapq.heappush(intervals, [dist, l, r])
                    found = True
                    break
                else:
                    temp.append([dist, l, r])
            for t in temp:
                heapq.heappush(intervals, t)
            if not found:
                ans.append(-1)
        return ans

# Optimized Approach
def minInterval(intervals, queries):

    ans = [-1] * len(queries) # init ans array with -1 till size of queries
    intervals = sorted(intervals, key=lambda x: x[0]) # sort intervals by start time
    queries = [[i, val] for i, val in enumerate(queries)] # create index, val pairs for each query item

    queries = sorted(queries, key=lambda x: x[1]) # sort the queries array by actual query val in ascending order

    i = 0
    min_heap = []
    for idx, q in queries:
        
        while i < len(intervals) and intervals[i][0] <= q:
            # if current interval start (intervals[i][0]) less than current query time, 
            # we add [r-l + 1, current interval end time] to heap
            heapq.heappush(min_heap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
            i+=1 # increment i
        
        while min_heap and min_heap[0][1] < q:
            # if top of heap ends before current query, it will not be useful in future too 
            # as all future queries will be bigger than current query due to sorting
            # so we pop it out from the heap
            heapq.heappop(min_heap)
        # if the heap is not empty, we update the ans[idx] with heap's top r-l+1 value
        if len(min_heap) > 0:
            ans[idx] = min_heap[0][0]
    return ans