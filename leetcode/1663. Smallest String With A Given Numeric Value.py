class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        
        res = ''
        for i in range(n-1, -1, -1):
            if k == 0:
                res = 'a' + res
            elif k < 25:
                res = chr(ord('a')+k) + res
                k = 0
            else:
                res = 'z' + res
                k -= 25

        return res
        
