from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        
        for [x, y] in points:
            heappush(h, (-x ** 2 - y **2, x, y))
            if len(h) > k:
                heappop(h)
        
        return [[x, y] for [_, x, y] in h]
        
