# Title: 1448. Count Good Nodes in Binary Tree
# Difficulty: Medium
# Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.good_nodes = 0
        self.dfs(root, float('-inf'))

        return self.good_nodes

    # transverse thorugh using depth-first search
    def dfs(self, node: TreeNode, max_val) -> None:
        if node:
            if node.val >= max_val:
                self.good_nodes += 1
            self.dfs(node.left, max(max_val, node.val))
            self.dfs(node.right, max(max_val, node.val))
