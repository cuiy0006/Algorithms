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
        s0 = s
        s = ''
        for c in s0:
            if c != ' ':
                s += c
        
        stack = []
        curr = ''
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                curr += c
                i += 1
            elif c == '+' or c == '-':
                stack.append(int(curr))
                curr = ''
                curr += c
                i += 1
            else:
                stack.append(int(curr))
                curr = ''
                j = i + 1
                while j < len(s):
                    if s[j].isdigit():
                        j += 1
                    else:
                        break
                second = int(s[i+1:j])
                if c == '*':
                    curr = stack.pop() * second
                else:
                    curr = int(stack.pop() / second)
                i = j

        if curr != '':
            stack.append(int(curr))
            
        return sum(stack)
