# Title: 142. Linked List Cycle II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        node = head
        while node:
            if node in visited_nodes:
                return node
            visited_nodes.add(node)
            node = node.next
        return None
