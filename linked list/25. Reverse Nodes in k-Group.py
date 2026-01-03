# HARD
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Approach 1 

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        # Step 1: Store nodes in an array
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Step 2: Reverse nodes in chunks of k
        n = len(nodes)
        for i in range(0, n, k):
            if i + k <= n:          # only reverse full k groups
                nodes[i:i+k] = reversed(nodes[i:i+k])

        # Step 3: Reconnect nodes
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]

        nodes[-1].next = None

        return nodes[0]
