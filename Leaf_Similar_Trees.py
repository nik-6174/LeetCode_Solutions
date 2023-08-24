# Title: 872. Leaf-Similar Trees
# Difficulty: Easy
# Problem: https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaf_values_1 = []
        self.leaf_values_2 = []

        self.find_leaf_values_1(root1)
        self.find_leaf_values_2(root2)

        return tuple(self.leaf_values_1) == tuple(self.leaf_values_2)


    def find_leaf_values_1(self, node):
        if node:
            if (not node.left) and (not node.right):
                self.leaf_values_1.append(node.val)
            self.find_leaf_values_1(node.left)
            self.find_leaf_values_1(node.right)
    
    def find_leaf_values_2(self, node):
        if node:
            if (not node.left) and (not node.right):
                self.leaf_values_2.append(node.val)
            self.find_leaf_values_2(node.left)
            self.find_leaf_values_2(node.right)
