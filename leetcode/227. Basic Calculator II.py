class Solution:
    def calculate(self, s: str) -> int:
        sign = '+'
        curr = ''
        stack = []
        s = s.strip()
        for i, c in enumerate(s):
            if c.isdigit():
                curr += c
            if not c.isdigit() or i == len(s) - 1:
                if curr == '' and curr == '-':
                    sign = c
                    continue
                if c == ' ':
                    continue
                if sign == '+':
                    stack.append(int(curr))
                elif sign == '-':
                    stack.append(-int(curr))
                elif sign == '*':
                    stack.append(stack.pop() * int(curr))
                elif sign == '/':
                    num = stack.pop()
                    isPositive = num > 0
                    res = abs(num) // int(curr)
                    if not isPositive:
                        res = -res
                    stack.append(res)
                curr = ''
                sign = c
        return sum(stack)
