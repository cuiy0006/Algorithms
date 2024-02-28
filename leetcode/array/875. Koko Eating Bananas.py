class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(cap):
            hour = 0
            for i in range(len(piles)):
                if piles[i] % cap == 0:
                    consume = piles[i] // cap
                else:
                    consume = piles[i] // cap + 1
                hour += consume
                if hour > h:
                    return False
            return True
        
        i = 1
        j = max(piles)+1
        while i < j:
            mid = (i+j)//2
            if can_eat(mid):
                j = mid
            else:
                i = mid + 1
        if can_eat(i):
            return i
        else:
            return i + 1