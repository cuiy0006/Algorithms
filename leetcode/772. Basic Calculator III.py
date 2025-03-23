class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(s):
            tmp = ''
            for c in s:
                if c != ' ':
                    tmp += c
            s = tmp
            if s[0] != '+' and s[0] != '-':
                s = '+' + s
            i = 0
            stack = []
            ops = {'+', '-', '*', '/'}
            while i < len(s):
                j = i+1
                if s[j] == '+' or s[j] == '-':
                    j += 1
                while j < len(s) and s[j] not in ops:
                    j += 1
                num = int(s[i+1:j])
                if s[i] == '+':
                    stack.append(num)
                elif s[i] == '-':
                    stack.append(-num)
                elif s[i] == '*':
                    stack[-1] = stack[-1]*num
                else:
                    stack[-1] = int(stack[-1]/num)
                i = j
            return sum(stack)
        
        curr = ''
        stack = []
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = ''
            elif c == ')':
                curr = stack.pop() + str(evaluate(curr))
            else:
                curr += c
        print(curr)
        return evaluate(curr)
