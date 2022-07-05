from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        heappush(h, 1)
        seen = set()

        for i in range(n):
            num = heappop(h)
            if i == n-1:
                return num
            
            for next_num in (num*2, num*3, num*5):
                if next_num not in seen:
                    seen.add(next_num)
                    heappush(h, next_num)
        
        return 1
