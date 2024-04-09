class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        lst = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    lst.append(i)
                else:
                    stack.pop()
        lst += stack
        res = ''
        i = 0
        for j in range(len(s)):
            if i == len(lst) or j != lst[i]:
                res += s[j]
            else:
                i += 1
        return res
