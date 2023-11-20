# Title: 150. Evaluate Reverse Polish Notation
# Difficulty: Medium
# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/description

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['/', '*', '+', '-']

        for i in range(len(tokens)):
            if tokens[i] in operators:
                operator = tokens[i]
                if operator == '/':
                    B = stack.pop()
                    A = stack.pop()
                    res = int(A / B)
                if operator == '*':
                    res = stack.pop() * stack.pop()
                if operator == '+':
                    res = stack.pop() + stack.pop()
                if operator == '-':
                    res = -stack.pop() + stack.pop()
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]
