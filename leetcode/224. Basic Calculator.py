class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        num = 0
        sign = 1
        res = 0
        
        for c in s:
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            elif c == '+' or c == '-':
                res += sign * num
                num = 0
                sign = stack[-1]
                if c == '-':
                    sign *= -1

            elif c == '(':
                stack.append(sign)
            elif c == ')':
                res += sign * num
                num = 0
                sign = stack.pop()

        return res + sign * num
