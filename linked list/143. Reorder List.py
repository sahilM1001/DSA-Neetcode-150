# MEDIUM
# https://leetcode.com/problems/reorder-list/description/

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Approach

def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        cur = head
        # iterate over the list and copy it to an array
        while cur != None:
            arr.append(cur)
            cur = cur.next
        
        l = 0 # init left pointer at 0
        r = len(arr) - 1 # init right pointer at len(arr) - 1
        while l < r:
            arr[l].next = arr[r] # change arr[l].next to point to arr[right]
            l += 1 # increment l

            if l >= r: # if l >= r stop processing
                break
            arr[r].next = arr[l] # change arr[r].next to new arr[l]
            r-=1 # decrease right pointer by 1
        arr[l].next = None #arr[l] will be at end, so set arr[l].next to None