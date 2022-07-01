class Solution:
    def calculate(self, s: str) -> str:
        ops = ('+', '-', '*', '/')
        
        def evaluate(s):
            stack = []
            if s[0] != '+' and s[0] != '-':
                s = '+' + s
            i = 0
            while i < len(s):
                j = i+1
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
                    stack[-1] = int(stack[-1]/curr)
                i = j
            return str(sum(stack))
            
        
        stack = []
        curr = ''
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = ''
            elif c == ')':
                curr = evaluate(curr)
                if len(stack) != 0:
                    curr = stack.pop() + curr
            else:
                curr += c

        return int(evaluate(curr))
