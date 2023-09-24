# Title: 61. Rotate List
# Difficulty: Medium
# Problem: https://leetcode.com/problems/rotate-list/description/

## By rotating the nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        node = head

        # count number of nodes
        count = 1

        # go to the last node
        while node.next:
            node = node.next
            count += 1
        
        # initilize the next node to last as the head to complete a cycle 
        node.next = head

        count -= (k % count) + 1

        # find the new end node
        end_node = head

        while count:
            end_node = end_node.next
            count -= 1
        
        # make the next node as start node (head)
        new_head = end_node.next
        
        # break the cycle
        end_node.next = None

        return new_head


## By rotating the values

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        values, node = [], head

        while node:
            values.append(node.val)
            node = node.next

        count = len(values)
        k = (k % count) # crop out multiple complete rotations

        node = head
        for i in range(count):
            node.val = values[(count - k + i) % count]
            node = node.next

        return head
