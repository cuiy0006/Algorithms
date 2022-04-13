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

    
    
    
    
    
class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(s) -> int:
            s0 = s
            s = ''
            for c in s0:
                if c != ' ':
                    s += c

            res = 0
            i = 0
            s = '+' + s
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    continue
                if s[i] == '+' or s[i] == '-':
                    j = i + 1
                    if s[j] == '+' or s[j] == '-':
                        j += 1
                    
                    while j < len(s) and s[j] != '+' and s[j] != '-':
                        j += 1

                    num = int(s[i+1:j])
                    if s[i] == '+':
                        res += num
                    else:
                        res -= num
                    i = j
                else:
                    i += 1
            return res
        
        stack = []
        i = 0
        curr = ''
        while i < len(s):
            if s[i] == '(':
                stack.append(curr)
                curr = ''
            elif s[i] == ')':
                num = evaluate(curr)
                curr = stack.pop() + str(num)
            else:
                curr += s[i]
            i += 1
        
        return evaluate(curr)
