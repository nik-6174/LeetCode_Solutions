# Title: 105. Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # create a node
        node = TreeNode(val=preorder[0])

        # find the node value and it's index
        pivot = inorder.index(node.val)

        # find the right and the left subtree
        if pivot != 0:
            node.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        if pivot != len(inorder) - 1:
            node.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])
        
        return node
