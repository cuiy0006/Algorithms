class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dic = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: int(x/y)
        }
        for token in tokens:
            if token in dic:
                num1 = stack.pop()
                num2 = stack.pop()
                num = dic[token](num2, num1)
                stack.append(num)
            else:
                stack.append(int(token))
        return stack[0]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    num1 = num1 + num2
                elif token == '-':
                    num1 = num1 - num2
                elif token == '*':
                    num1 = num1 * num2
                else:
                    num1 = int(num1 / num2)
                stack.append(num1)
            else:
                stack.append(int(token))
        return stack.pop()
