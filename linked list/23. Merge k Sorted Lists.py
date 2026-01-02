# HARD
# https://leetcode.com/problems/merge-k-sorted-lists/description/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6

# Approach 
# As we want the min at each iteration, a min heap is a good option here. 


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    import heapq
    my_heap = []

    # We init the min heap with heads of each list at start 
    for i, node in enumerate(lists):
        if node:
            # pushing node.val, node list/source, and node to the heap
            heapq.heappush(my_heap, (node.val, i, node))
    dummy = ListNode() # create dummy node
    current = dummy 

    while my_heap: # run loop till heap is not empty
        val, source, node = heapq.heappop(my_heap) # pop the min value from the heap
        current.next = node # put current.next as the popped node
        current = current.next # increment current to current.next
 
        if node.next: 
            # if popped node has a next val
            # push node.val, node list/source, and node to the heap
            heapq.heappush(my_heap, (node.next.val, source, node.next))
    
    #return dummy.next as that will be the head
    return dummy.next
    