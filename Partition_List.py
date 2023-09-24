# Title: 86. Partition List
# Diffficulty: Medium
# Problem: https://leetcode.com/problems/partition-list/description/

## By changing the values

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        # store all the values
        node, values = head, []
        while node:
            values.append(node.val)
            node = node.next
        
        # fill the indexes of values into either left (smaller) or right (greater or equal to) of x
        left, right = [], []

        for i in range(len(values)):
            if values[i] < x:
                left.append(i)
            else:
                right.append(i)
        
        # fill values from left to right
        node = head
        for i in left + right:
            node.val = values[i]
            node = node.next

        return head

## By changing the nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        # create two left and right node heads
        left, right = ListNode(), ListNode()
        node, node1, node2 = head, left, right
        
        # add nodes in either left (node value < x) or right (node value >= x)
        while node:
            if node.val < x:
                node1.next = node
                node1 = node1.next
            else:
                node2.next = node
                node2 = node2.next
            node = node.next
        # add the right to the end of left
        node1.next = right.next
        # end the right with None
        node2.next = None

        return left.next
