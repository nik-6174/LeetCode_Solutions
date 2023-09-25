# Title: 129. Sum Root to Leaf Numbers
# Difficulty: Medium
# Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # define required variables
        self.sum = 0

        # define recurrsive function
        def sumHelper(node, num):
            if node:
                num = num * 10 + node.val
                if (not node.left) and (not node.right):
                    self.sum += num
                    return
                sumHelper(node.left, num)
                sumHelper(node.right, num)
        
        sumHelper(root, 0)
        
        return self.sum

        
