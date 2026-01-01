# MEDIUM
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


# Approach 
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        front = head
        cur = head
        i = 0
        while i < n:
            front = front.next
            i+=1

        if front == None:
            head = head.next
            return head
        while front.next != None:
            front = front.next
            cur = cur.next
        
        cur.next = cur.next.next
        return head

