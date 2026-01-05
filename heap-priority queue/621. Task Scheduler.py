# MEDIUM
# https://leetcode.com/problems/task-scheduler/description/

# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Approach


from collections import Counter, deque
import heapq

def leastInterval(tasks, n):
    time = 0
    count = Counter(tasks) # count frequency of each character

    max_heap = [-cnt for cnt in count.values()] # create a max heap with char's frequency val
    heapq.heapify(max_heap)
    q = deque()

    while max_heap or q:
        time += 1 # for each iteration increase time by 1

        if max_heap:
            cnt = 1 + heapq.heappop(max_heap) # pop the highest val from the heap and add + 1
            if cnt: # if count is not zero
                q.append([cnt, time+n]) # append count, time + n (when count can be used again) to queue
        if q and q[0][1] == time: 
            # if q[0]'s time == current time, it means the top q val is available for reuse from next iteration
            # so we will add it to the heap again
            heapq.heappush(max_heap, q.popleft()[0])
    return time