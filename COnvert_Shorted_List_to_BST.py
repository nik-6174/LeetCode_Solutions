# Title: 
# Difficulty: Medium
# Problem: 

## Using Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # store the elements in a list
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        # create the tree nodes using recurrsive fucntion
        def createTree (left, right):
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(val=nums[mid])
                node.right = createTree(mid + 1, right)
                node.left = createTree(left, mid-1)
                return node
        
        return createTree(0, len(nums)-1)

## without using lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        
        # intitialize three pointers
        slow = fast = head
        preMid = None

        while fast and fast.next:
            preMid = slow
            slow = slow.next
            fast = fast.next.next
        
        # create the tree node for the middle node in the linked list
        root = TreeNode(val=slow.val)

        if preMid:
            preMid.next = None
            root.left = self.sortedListToBST(head)
        
        if slow.next:
            root.right = self.sortedListToBST(slow.next)
        
        return root
