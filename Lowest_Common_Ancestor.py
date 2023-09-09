# Title: 236. Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.q = q
        self.p = p
        self.node = None
        self.flag = True
        self.search(root)
        return self.node
        
    
    def search(self, root: Optional[TreeNode]) -> tuple[bool]:
        if root and self.flag:
            has_q = False
            has_p = False
            if root == self.q:
                has_q = True
            if root == self.p:
                has_p = True
            if root.left:
                value1 = self.search(root.left)
                if value1[0]:
                    has_p = True
                if value1[1]:
                    has_q = True
            if root.right:
                value2 = self.search(root.right)
                if value2[0]:
                    has_p = True
                if value2[1]:
                    has_q = True
            if (has_p and has_q) and self.flag:
                self.node = root
                self.flag = False
            return (has_p, has_q)
        return (False, False)
