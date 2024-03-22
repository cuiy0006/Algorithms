class Solution:
    def calculate(self, s: str) -> int:
        tmp = ''
        for c in s:
            if c != ' ':
                tmp += c
        s = tmp
        if s[0] != '+' and s[0] != '-':
            s = '+' + s
        stack = []
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[j].isnumeric():
                j += 1
            num = s[i+1:j]
            if s[i] == '+':
                stack.append(int(num))
            elif s[i] == '-':
                stack.append(-int(num))
            elif s[i] == '*':
                stack[-1] = stack[-1] * int(num)
            else:
                stack[-1] = int(stack[-1] / int(num))
            i = j

        return sum(stack)