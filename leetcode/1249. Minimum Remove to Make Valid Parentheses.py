class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = []
        delete = []
        
        for i, c in enumerate(s):
            if len(left) == 0 and c == ')':
                delete.append(i)
            else:
                if c == '(':
                    left.append(i)
                elif c == ')':
                    left.pop()
        
        i = 0
        j = 0
        indexes = []
        while i < len(delete) and j < len(left):
            if delete[i] < left[j]:
                indexes.append(delete[i])
                i += 1
            else:
                indexes.append(left[j])
                j += 1
        
        while i < len(delete):
            indexes.append(delete[i])
            i += 1
        while j < len(left):
            indexes.append(left[j])
            j += 1
            
        res = ''
        i = 0
        for idx in indexes:
            res += s[i:idx]
            i = idx+1
        res += s[i:]
        return res
        




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
            
