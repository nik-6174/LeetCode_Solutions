# Title: 230. Kth Smallest Element in a BST
# Difficulty: Medium
# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # store the inorder values in a list
        self.kth_min = 0
        self.counter = -k

        # perform dfs to transverse through the tree
        def transverse(node: Optional[TreeNode]):
            if node:
                transverse(node.left)
                self.counter += 1
                if not self.counter:
                    self.kth_min = node.val
                transverse(node.right)

        # transverse through the list to get the sorted array
        transverse(root)
        return self.kth_min
