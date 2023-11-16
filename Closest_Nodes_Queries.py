# Title: 2476. Closest Nodes Queries in a Binary Search Tree
# Difficulty: Medium
# Problem: https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        res, nums = [], []

        # find the inorder transversal (shorted list)
        def dfs(node):
            if node:
                dfs(node.left)
                nums.append(node.val)
                dfs(node.right)
        dfs(root)

        # when there's only one node in the  tree
        if len(nums) == 1:
            return [[query, query] if query == nums[0] else [-1, -1] for query in queries]
        
        for query in queries:
            temp = []
            index = bisect.bisect_left(nums, query)
            if index == len(nums): # the query is greater than any element in the tree
                res.append([nums[-1], -1])
            elif nums[index] == query: # when query found in the tree
                res.append([query, query])
            elif index == 0: # when the element is smaller than any element in the tree
                res.append([-1, nums[0]])
            else: # we append the min(i) and max(i) into the result
                res.append([nums[index-1], nums[index]])

        return res
