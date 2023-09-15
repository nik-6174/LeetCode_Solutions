# Title: 138. Copy List with Random Pointer
# Difficulty: Medium
# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_nodes = [None]
        node = head
        # create a dummy node head
        new_node = new_head = Node(0)
        while node:
            # make a list of all original nodes
            original_nodes.append(node)
            new_node.next = Node(node.val)
            new_node = new_node.next
            node = node.next
        # delete the dummy head
        new_head = new_head.next
        node = head
        # list to store the index of the node for each random node
        node_number = []

        while node:
            node_number.append(original_nodes.index(node.random))
            node = node.next
        node = new_head

        copy_nodes = [None]
        while node:
            # make a list of all copied nodes
            copy_nodes.append(node)
            node = node.next
        
        node = new_head
        for node_idx in node_number:
            # assign random node based on the nodes from original linked list
            node.random = copy_nodes[node_idx]
            node = node.next
        # return the new copied linked list
        return new_head
        
