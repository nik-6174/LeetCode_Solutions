# Title: 173. Binary Search Tree Iterator
# Difficulty: Medium
# Problem: https://leetcode.com/problems/binary-search-tree-iterator/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def gen(node):
            if node.left:
                yield from gen(node.left)
            
            yield node

            if node.right:
                yield from gen(node.right)

        self.gen = gen(root)
        self.cur = next(self.gen)
        self.has_next = True

    def next(self) -> int:
        result = self.cur.val

        try:
            self.cur = next(self.gen)
        except StopIteration:
            self.has_next = False

        return result

    def hasNext(self) -> bool:
        return self.has_next


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
