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
            curr = 0
            i = 0
            while i < len(s):
                c = s[i]
                j = i+1
                if s[j] == '+' or s[j] == '-':
                    j += 1
                while j < len(s) and s[j].isnumeric():
                    j += 1
                if c == '+':
                    curr += int(s[i+1:j])
                else:
                    curr -= int(s[i+1:j])
                i = j
            return str(curr)
                    
        curr = ''
        stack = []
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = ''
            elif c == ')':
                curr = stack.pop() + evaluate(curr)
            else:
                curr += c
        
        return int(evaluate(curr))
