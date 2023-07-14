# Title: 328. Odd Even Linked List (Leetcode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        even, odd = [], []
        # collect the even and odd values
        node = head
        while node and node.next:
            odd.append(node.val)
            even.append(node.next.val)
            node = node.next.next
        # if node.next was None
        if node:
            odd.append(node.val)

        # add even elements after odd elements
        odd += even
        idx = 0
        node = head
        while node:
            node.val = odd[idx]
            node = node.next
            idx += 1
        return head

