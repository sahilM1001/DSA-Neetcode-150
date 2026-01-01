# EASY
# https://leetcode.com/problems/reverse-linked-list/description/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    next_1 = None
    prev = None

    while curr != None:
        next_1 = curr.next 
        curr.next = prev
        prev = curr
        curr = next_1 
    head = prev
    return head