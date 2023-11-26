# Title: 116. Populating Next Right Pointers in Each Node
# Difficulty: Medium
# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        queue = deque([root])
        
        while queue:
            n = len(queue)
            prev = None
            # transverse the nodes from top to down
            for i in range(n):
                node = queue.popleft()
                # assign the next pointer to the previous node as the current node
                if prev:
                    prev.next = node
                prev = node # update the previous node as the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
