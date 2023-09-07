# Title: 71. Simplify Path
# Difficulty: Medium
# Problem: https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = list(path.split('/'))
        stack = []
        for i in arr:
            if not i or (i == '.'):
                continue
            if i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
        
