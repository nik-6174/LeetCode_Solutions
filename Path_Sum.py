# Title: 113. Path Sum II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.dfs(root, [], targetSum)

        return self.res

    
    def dfs(self, node: Optional[TreeNode], values: List[int], sum: int) -> None:
        if not node:
            return
        if not node.left and not node.right:
            if node.val == sum:
                self.res.append(values + [node.val])
            return
        self.dfs(node.left, values + [node.val], sum - node.val)
        self.dfs(node.right, values + [node.val], sum - node.val)


