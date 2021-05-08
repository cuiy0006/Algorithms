class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = set()
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    invalid.add(i)
                else:
                    stack.pop()
        
        for idx in stack:
            invalid.add(idx)
        
        res = ''
        for i, c in enumerate(s):
            if i not in invalid:
                res += c
        return res
            
