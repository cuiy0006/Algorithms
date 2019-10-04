class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        if s == '':
            return res
        
        def isPalin(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def helper(idx, tmp):
            if idx == len(s):
                res.append(tmp[:])
                return
            
            for i in range(idx, len(s)):
                if isPalin(idx, i):
                    tmp.append(s[idx: i + 1])
                    helper(i + 1, tmp)
                    tmp.pop()
        helper(0, [])
        return res
