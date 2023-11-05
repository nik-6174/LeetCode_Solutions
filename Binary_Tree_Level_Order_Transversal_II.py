# Title: 107. Binary Tree Level Order Traversal II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import array
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue, res = [root], []
        while queue:
            curr_level = array.array('h')
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.insert(0, curr_level)
        return res
