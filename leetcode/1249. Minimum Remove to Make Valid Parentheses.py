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
        indexes = delete + left
            
        res = ''
        i = 0
        for idx in indexes:
            res += s[i:idx]
            i = idx+1
        res += s[i:]
        return res
        
