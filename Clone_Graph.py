# Title: 33. Clone Graph
# Difficulty: Medium
# Problem: https://leetcode.com/problems/clone-graph/description

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        # find all the values and their neighbor values
        nodeNeighbors = {}
        def dfs(node):
            if node.val in nodeNeighbors:
                return
            nodeNeighbors[node.val] = set()
            for neighbor in node.neighbors:
                nodeNeighbors[node.val].add(neighbor.val)
                dfs(neighbor)
        dfs(node)

        # Create new node for each value
        val_to_node = {}
        for val in nodeNeighbors:
            newNode = Node(val=val)
            val_to_node[val] = newNode
        
        # fill the neighbors
        for val in nodeNeighbors:
            curr_node = val_to_node[val]
            for neighbor in nodeNeighbors[val]:
                curr_node.neighbors.append(val_to_node[neighbor])
        
        return val_to_node[node.val]
