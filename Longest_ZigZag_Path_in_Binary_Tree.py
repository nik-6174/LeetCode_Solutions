# Title: 1372. Longest ZigZag Path in a Binary Tree
# Diffficulty: Medium
# Problem: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        self.zigzag(root.left, 'left', 0)
        self.zigzag(root.right, 'right', 0)

        return self.max_len
        

    def zigzag(self, node: Optional[TreeNode], direction: str, curr: int) -> None:
        if node:
            curr += 1
            self.max_len = max(curr, self.max_len)

            if direction == 'left':
                self.zigzag(node.right, 'right', curr)
                self.zigzag(node.left, 'left', 0)
            else:
                self.zigzag(node.left, 'left', curr)
                self.zigzag(node.right, 'right', 0)


