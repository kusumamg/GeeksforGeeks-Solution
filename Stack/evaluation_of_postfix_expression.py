class Solution:
    def evaluatePostfix(self, arr):
        stack = []

        for ch in arr:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()

                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                elif ch == '/':
                    stack.append(a // b)
                elif ch == '^':
                    stack.append(a ** b)

        return stack[-1]