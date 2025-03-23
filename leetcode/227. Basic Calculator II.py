class Solution:
    def calculate(self, s: str) -> int:
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
            while j < len(s) and s[j] not in ops:
                j += 1
            num = int(s[i+1:j])
            if s[i] == '+':
                stack.append(num)
            elif s[i] == '-':
                stack.append(-num)
            elif s[i] == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            i = j
        return sum(stack) 
