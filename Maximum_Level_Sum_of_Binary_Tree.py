# Title: 1161. Maximum Level Sum of a Binary Tree
# Difficulty: Medium
# Problem: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

# efficient memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.level_sum = []
        self.levelSumHelper(root, 1)

        return self.level_sum.index(max(self.level_sum)) + 1


    def levelSumHelper(self, node: Optional[TreeNode], level) -> None:
        if node:
            if len(self.level_sum) < level:
                self.level_sum.append(node.val)
            else:
                self.level_sum[level-1] += node.val
            self.levelSumHelper(node.left, level+1)
            self.levelSumHelper(node.right, level+1)

# efficient time

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float("-inf")
        max_level = 0

        level = 1
        queue = deque([root])

        while queue:
            level_sum = sum(node.val for node in queue)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return max_level
