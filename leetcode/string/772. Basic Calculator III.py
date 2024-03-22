class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(s):
            if s[0] != '+' and s[0] != '-':
                s = '+' + s
            i = 0
            stack = []
            while i < len(s):
                j = i+1
                if s[j] == '+' or s[j] == '-':
                    j += 1
                while j < len(s) and s[j].isnumeric():
                    j += 1
                num = int(s[i+1:j])
                if s[i] == '+':
                    stack.append(num)
                elif s[i] == '-':
                    stack.append(-num)
                elif s[i] == '*':
                    stack[-1] = stack[-1] * num
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
