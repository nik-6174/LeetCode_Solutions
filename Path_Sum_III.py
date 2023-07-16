# Title: 437. Path Sum III (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.dfs(root, targetSum, [])
        return self.count

    def dfs(self, node, targetSum, path):
        if node:
            # Add the current node's value to the path
            path.append(node.val)
            
            # Check if any subpath of the current path has a sum equal to the target sum
            total = 0
            for i in range(len(path) - 1, -1, -1):
                total += path[i]
                if total == targetSum:
                    self.count += 1
            
            # Recurse on the left and right child nodes
            self.dfs(node.left, targetSum, path)
            self.dfs(node.right, targetSum, path)
            
            # Remove the current node's value from the path to backtrack
            path.pop()
