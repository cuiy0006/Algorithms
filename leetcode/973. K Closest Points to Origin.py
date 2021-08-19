from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heappush(heap, (-dist, point[0], point[1]))
            if len(heap) > k:
                heappop(heap)
                
        res = [[x, y] for _, x, y in heap]
        return res
