# Title: 2130. Maximum Twin Sum of a Linked List (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Solution using stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # initialize two pointers for the end and the mid node
        node1 = head
        node2 = head
        first_half = [] # initialize the stack
        while node2 and node2.next: # node2 -> goes to the end
            first_half.append(node1.val) # store the value
            node1 = node1.next # node1 -> goes to the mid
            node2 = node2.next.next
        max_sum = float('-inf')
        while node1: # start from the mid
            if node1.val + first_half[-1] > max_sum: # check the twin sum
                max_sum = node1.val + first_half[-1] # update the max_sum
            node1 = node1.next # go to the next node
            first_half.pop() # pop the stack
        
        return max_sum
        
# Solution using array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # initialize two pointers for the end and the mid node
        node = head
        arr = []
        while node:
            arr.append(node.val) # store the value in a list
            node = node.next
        # find the twin sum of the array till the mid element
        for i in range(len(arr)//2):
            arr[i] += arr[len(arr)-1-i]

        return max(arr[:len(arr)//2]) # return the maximum twin sum

      
