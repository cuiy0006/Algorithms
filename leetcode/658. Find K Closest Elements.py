class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = [(abs(num - x), num) for num in arr]
        lst.sort(key=lambda tp: tp[0])
        
        res = [num for distance, num in lst[:k]]
        return sorted(res)
      
      
      
 

from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            distance = abs(num - x)
            if len(heap) < k:
                heappush(heap, (-distance, num))
            else:
                if distance < -heap[0][0]:
                    heappop(heap)
                    heappush(heap, (-distance, num))
        
        res = []
        while len(heap) != 0:
            res.append(heappop(heap)[1])
        
        res.sort()
        return res
