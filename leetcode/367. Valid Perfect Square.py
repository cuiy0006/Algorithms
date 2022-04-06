class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        j = num // 2 + 1
        while i < j:
            mid = (i + j) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                j = mid
            else:
                i = mid + 1
        
        return i * i == num
