# Title: 700. Search in a Binary Search Tree
# Difficulty: Easy
# Problem: https://leetcode.com/problems/search-in-a-binary-search-tree/description/

## Memory Efficient (using recurrsion)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        if root.val > val:
            if root.left:
                return self.searchBST(root.left, val)
            else:
                return None
        else:
            if root.right:
                return self.searchBST(root.right, val)
            else:
                return None

## Runtime Efficient

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right
        return None
