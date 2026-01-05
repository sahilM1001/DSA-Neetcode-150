# HARD
# https://leetcode.com/problems/find-median-from-data-stream/description/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Approach
import heapq

class MedianFinder:

    def __init__(self):
        self.small_heap= []
        self.large_heap = []
        

    def addNum(self, num: int) -> None:
        if self.large_heap and num > self.large_heap[0]:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, -1 * num)

        if len(self.large_heap) > len(self.small_heap) + 1:
            val = -1 * heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, val)
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]
        if len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]
        return (-1 * self.small_heap[0] + self.large_heap[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()