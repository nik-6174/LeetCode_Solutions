# Title: 449. Serialize and Deserialize BST
# Difficulty: Medium
# Problem: https://leetcode.com/problems/serialize-and-deserialize-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        values = []
        # fill the node values in preorder sequence
        def dfs(node):
            if not node:
                values.append('None')
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ",".join(values)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        values = deque(data.split(","))
        # create the BST again from the preorder array
        def dfs():
            value = values.popleft()
            if value == 'None':
                return None
            node = TreeNode(value)
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
