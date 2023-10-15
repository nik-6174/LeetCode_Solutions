# Title: 106. Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Medium
# Problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}

        for i, val in enumerate(inorder):
            inorder_map[val] = i
        
        def buildHelper(left, right) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # create a node and add it's value
            node = TreeNode(val=postorder.pop())

            # find the node value and it's index
            pivot = inorder_map[node.val]

            # create the left and the right subtree
            node.right = buildHelper(pivot + 1, right)
            node.left = buildHelper(left, pivot-1)
            return node
        
        return buildHelper(0, len(postorder)-1)
