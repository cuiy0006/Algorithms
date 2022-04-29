class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/')
        
        res = []
        for p in lst:
            if p == '':
                continue
            elif p == '.':
                continue
            elif p == '..':
                if len(res) != 0:
                    res.pop()
            else:
                res.append(p)
        
        return '/' + '/'.join(res)
