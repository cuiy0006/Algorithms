from heapq import heappush, heappop

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        max_val = -sys.maxsize
        
        for x, y in points:
            while len(heap) != 0 and x - heap[0][1] > k:
                heappop(heap)
                
            if len(heap) != 0:
                max_val = max(max_val, x + y - heap[0][0])
                
            heappush(heap, (x - y, x))
        
        
        return max_val
