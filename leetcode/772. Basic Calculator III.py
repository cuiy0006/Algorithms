class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(s):
            stack = []
            i = 0
            s = '+' + s
            while i < len(s):
                if s[i] == '+' or s[i] == '-':
                    j = i + 1
                    if s[j] == '+' or s[j] == '-':
                        j += 1
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    num = int(s[i+1:j])
                    if s[i] == '-':
                        num = -num
                    stack.append(num)
                    i = j
                elif s[i] == '*' or s[i] == '/':
                    j = i + 1
                    if s[j] == '+' or s[j] == '-':
                        j += 1
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    num = int(s[i+1:j])
                    if s[i] == '*':
                        stack[-1] *= num
                    else:
                        stack[-1] = int(stack[-1] / num)
                    i = j
            return str(sum(stack))
                
        
        stack = []
        curr = ''
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = ''
            elif c == ')':
                curr = stack.pop() + evaluate(curr)
            else:
                curr += c
                
        return int(evaluate(curr))
