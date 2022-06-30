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
    def calculate(self, s: str) -> str:
        def evaluate(s) -> str:
            origin = s
            s = ''
            for c in origin:
                if c != ' ':
                    s += c
            
            if s[0] != '+' and s[0] != '-':
                s = '+' + s
            
            curr = 0
            i = 0
            while i < len(s):
                j = i+1
                if s[j] == '+' or s[j] == '-':
                    j += 1
                while j < len(s) and (s[j] != '-' and s[j] != '+'):
                    j += 1
                other = s[i+1:j]
                if s[i] == '+':
                    curr += int(other)
                else:
                    curr -= int(other)
                i = j
                
            return str(curr)
            
        
        stack = []
        curr = ''
        for c in s:
            if c == '(':
                if curr != '':
                    stack.append(curr)
                    curr = ''
            elif c == ')':
                curr = evaluate(curr)
                if len(stack) != 0:
                    curr = stack.pop() + curr
            else:
                curr += c
        
        curr = evaluate(curr)
        return int(curr)
