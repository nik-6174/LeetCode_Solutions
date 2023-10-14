# Title: 637. Average of Levels in Binary Tree
# Difficulty: Medium
# Problem: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # inititalize a queue
        queue, res = deque(), []

        # start with the root
        queue.append(root)

        # go from top to down
        while queue:
            n = len(queue)
            totalSum = 0
            # pop all the nodes of the current level
            for _ in range(n):
                node = queue.popleft()
                if node:
                    totalSum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(totalSum/n)

        return res
