class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0, int(c ** 0.5) + 1):
            b = (c - a ** 2) ** 0.5
            if int(b) == b:
                return True
            if b <= a:
                return False
        return False
        
