class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(s):
            curr = ''
            stack = []
            i = 0
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    curr += c
                    i += 1
                elif c == '+' or c == '-':
                    if curr != '':
                        stack.append(int(curr))
                    curr = ''
                    j = i + 1
                    if s[j] == '+' or s[j] == '-':
                        j += 1
                    while j < len(s):
                        if s[j].isdigit():
                            j += 1
                        else:
                            break
                    curr = s[i+1:j]
                    if s[i] == '+':
                        curr = str(int(curr))
                    else:
                        curr = str(-int(curr))
                    i = j
                else:
                    j = i + 1
                    if s[j] == '+' or s[j] == '-':
                        j += 1
                    while j < len(s):
                        if s[j].isdigit():
                            j += 1
                        else:
                            break
                    second = int(s[i+1:j])
                    num = int(curr)
                    if c == '*':
                        curr = str(num * second)
                    else:
                        curr = str(int(num / second))
                    i = j

            if curr != '':
                stack.append(int(curr))

            return sum(stack)
        
        stack = []
        curr = ''
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = ''
            elif c == ')':
                second = str(evaluate(curr))
                curr = stack.pop() + second
            else:
                curr += c
        
        if curr != '':
            stack.append(curr)
            
        
        return evaluate(stack.pop())
