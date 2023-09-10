# Title: 450. Delete Node in a BST
# Difficulty: Medium
# Problem: https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: If the tree is empty, return None
        if not root:
            return root
        
        # Search for the node to be deleted
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Node with the key to be deleted found

            # Case 1: Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Case 2: Node with two children
            # Find the in-order successor (or predecessor) in the right (or left) subtree
            temp = self.minValueNode(root.right)

            # Copy the in-order successor's value to this node
            root.val = temp.val

            # Delete the in-order successor
            root.right = self.deleteNode(root.right, temp.val)

        return root

    def minValueNode(self, node):
        # Find the leftmost leaf node in the tree (the minimum value node)
        current = node
        while current.left:
            current = current.left
        return current
        
