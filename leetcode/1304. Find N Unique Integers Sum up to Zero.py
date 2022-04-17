class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 == 1:
            res.append(0)
        n = n // 2
        
        for i in range(1, n+1):
            res += [i, -i]
        
        return res
