# MEDIUM
# https://leetcode.com/problems/add-two-numbers/description/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Approach

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = l1
        cur_2 = l2
        str_1, str_2 = "", ""

        # loop to extract all digits from l1, append it to a string so it can be reversed easily
        while cur_1 != None:
            str_1+=str(cur_1.val)
            cur_1 = cur_1.next

        # loop to extract all digits from l2, append it to a string so it can be reversed easily
        while cur_2 != None:
            str_2+=str(cur_2.val)
            cur_2 = cur_2.next
        
        # reversing both s1 and s2 strings, converting them to int for addition, and again converting ans to str
        ans = str(int(str_1[::-1]) + int(str_2[::-1]))
        # reversing ans so we can create new list in the given output form (reversed)
        ans = ans[::-1] 
        
        new_node = ListNode(int(ans[0])) # creating base node with first digit of reversed ans
        new_head = new_node # creating new_head pointer
        for i in range(1, len(ans)): #loop from 1 to end of ans, create new node, append it to the list
            new_node_2 = ListNode(int(ans[i]))
            new_node.next = new_node_2
            new_node =new_node.next
        return new_head # return new_head pointer