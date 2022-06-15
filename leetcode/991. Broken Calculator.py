class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            if target % 2 == 1:
                target += 1
            else:
                target = target // 2
            res += 1
            
        return res + startValue - target
