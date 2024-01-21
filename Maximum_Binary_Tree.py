# Title: 654. Maximum Binary Tree
# Difficulty: Medium
# Problem: https://leetcode.com/problems/maximum-binary-tree/description/

# Using recurrssion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(val=nums[left])
            mid = left
            for i in range(left, right+1):
                if nums[i] > nums[mid]:
                    mid = i
            node = TreeNode(val = nums[mid])
            node.left = build_tree(left, mid-1)
            node.right = build_tree(mid+1, right)
            return node
        return build_tree(0, len(nums)-1)

# Using Stack (most efficient)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)       
            # If the stack is not empty and the current number is greater than the top of the stack,
            # we need to pop the stack until we find a node with a value greater than the current number.
            # The last popped node will be the parent of the current node.
            while stack and num > stack[-1].val:
                node.left = stack.pop()

            # If the stack is not empty, the top node is the parent of the current node.
            # We set the right child of the parent to be the current node.
            if stack:
                stack[-1].right = node

            # We push the current node onto the stack.
            stack.append(node)

        # The last node on the stack is the root of the tree.
        return stack[0]
