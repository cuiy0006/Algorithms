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

    
class Solution:
    def calculate(self, s: str) -> int:
        origin = s
        s = ''
        for c in origin:
            if c != ' ':
                s += c
        
        stack = []
        if s[0] != '+' and s[0] != '-':
            s = '+' + s
        
        ops = ('+', '-', '*', '/')
        
        i = 0
        while i < len(s):
            j = i + 1
            if s[j] == '+' or s[j] == '-':
                j += 1
            while j < len(s) and s[j] not in ops:
                j += 1
            curr = int(s[i+1:j])
            if s[i] == '+':
                stack.append(curr)
            elif s[i] == '-':
                stack.append(-curr)
            elif s[i] == '*':
                stack[-1] *= curr
            else:
                stack[-1] = int(stack[-1] / curr)
            i = j
        
        return sum(stack)
                
