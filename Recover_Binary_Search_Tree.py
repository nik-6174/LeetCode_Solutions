# Title: 99. Recover Binary Search Tree
# Difficulty: Medium
# Problem: https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr, new, values = [], {}, []

        # inorder transverse
        def transverse(node):
            if node:
                transverse(node.left)
                arr.append(node.val)
                transverse(node.right)
        
        # transverse the tree
        transverse(root)

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                values += [arr[i-1], arr[i]]
        
        # store the old and it's new value
        for i, num in enumerate(sorted(values)):
            if values[i] != num:
                new[values[i]] = num
        
        # swap the values
        def fill(node):
            if node:
                fill(node.left)
                if node.val in new:
                    node.val = new[node.val]
                fill(node.right)
        fill(root)
