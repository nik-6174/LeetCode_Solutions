# Title: 337. House Robber III
# Difficulty: Medium
# Problem: https://leetcode.com/problems/house-robber-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def transverse(node) -> List[int]:
            if not node:
                # return the max loot when robbing the current node, then without current node
                return [0, 0]
            # Find the the maximum value for the left and right subtree
            left = transverse(node.left)
            right = transverse(node.right)
            rob_current = left[1] + right[1] + node.val
            skip_current = max(left) + max(right)
            return [rob_current, skip_current]

        return max(transverse(root))
