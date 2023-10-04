# Title: 117. Populating Next Right Pointers in Each Node II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

## using DFS

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.levels = {}

        self.transverse(root, 0)
        return root
    
    def transverse(self, node: 'Node', level: int) -> None:
        if node:
            if level in self.levels:
                node.next = self.levels[level]
            self.levels[level] = node

            self.transverse(node.right, level + 1)
            self.transverse(node.left, level + 1)

## Using Queue

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        prev_node, prev_level = None, -1
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.pop()
            if level == prev_level:
                node.next = prev_node
            prev_node, prev_level = node, level
            if node.right:
                queue.appendleft((node.right, level + 1))
            if node.left:
                queue.appendleft((node.left, level + 1))

        return root
