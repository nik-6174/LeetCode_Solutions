# Title: 2095. Delete the Middle Node of a Linked List (Medium)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        left = head
        node = head.next.next
        while node and node.next:
            left = left.next
            node = node.next.next
        left.next = left.next.next
        return head
