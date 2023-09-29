# Title: 114. Flatten Binary Tree to Linked List
# Difficulty: Medium
# Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.curr = ListNode(next=root)
        self.transverse(root)

    def transverse(self, node):
        if node:
            self.curr.right = node
            self.curr = node
            right = node.right
            self.transverse(node.left)
            self.transverse(right)
            node.left = None
