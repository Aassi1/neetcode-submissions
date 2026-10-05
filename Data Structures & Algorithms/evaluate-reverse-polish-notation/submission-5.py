import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operator:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    c = b + a
                elif token == "-":
                    c = b - a
                elif token == "*":
                    c = b * a
                else:
                    c = math.trunc(b / a)

                stack.append(c)
            else:
                stack.append(int(token))

        return stack[-1]


        