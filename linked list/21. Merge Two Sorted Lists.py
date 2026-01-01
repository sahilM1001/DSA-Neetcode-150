# EASY
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Approach
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None and list2 == None:
        return None
    if list1 is not None and list2 == None:
        return list1
    if list2 is not None and list1 == None:
        return list2
    head, temp = None, None
    if list1.val < list2.val:
        temp = head = ListNode(list1.val)
        list1 = list1.next
    else:
        temp = head = ListNode(list2.val)
        list2 = list2.next
    while list1 != None and list2 != None:
        if list1.val < list2.val:
            temp.next = ListNode(list1.val)
            list1 = list1.next
        else:
            temp.next = ListNode(list2.val)
            list2 = list2.next
        temp = temp.next

    # add remaining nodes from list 1 if any
    while list1 != None:
        temp.next = ListNode(list1.val)
        list1 = list1.next
        temp = temp.next
    
    # add remaining nodes from list 2 if any
    while list2 != None:
        temp.next = ListNode(list2.val)
        list2 = list2.next
        temp = temp.next
    return head