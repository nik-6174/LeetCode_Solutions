# Title: 102. Binary Tree Level Order Traversal
# Difficulty: Medium
# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.transverseHelper(root, 1)
        return self.res

    def transverseHelper(self, node: Optional[TreeNode], level: int) -> None:
        if node:
            if level > len(self.res):
                self.res.append([node.val])
            else:
                self.res[level-1].append(node.val)
            self.transverseHelper(node.left, level+1)
            self.transverseHelper(node.right, level+1)
