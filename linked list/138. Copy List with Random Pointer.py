# MEDIUM
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Approach
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    map_1 = {None:None}
    temp = head
    # In first pass we populate the map by adding a new_node for every curr_node
    while temp != None:
        new_node = Node(temp.val)
        map_1[temp] = new_node
        temp = temp.next
    temp = head

    while temp != None:
        copy = map_1[temp] # get the copy node
        copy.next = map_1[temp.next] # set copy node.next as map_1[cur.next]
        copy.random = map_1[temp.random] # set copy node.random as map_1[cur.random]
        temp = temp.next # increment cur node
    return map_1[head] # return head from map_1 