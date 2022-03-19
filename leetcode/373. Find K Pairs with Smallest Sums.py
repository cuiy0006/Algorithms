from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        
        for num1 in nums1:
            for num2 in nums2:
                num = -(num1 + num2)
                
                heappush(h, (num, [num1, num2]))
                if len(h) > k:
                    heappop(h)
                    
                if num < h[0][0]:
                    break
        
        res = []
        while len(h) != 0:
            res.append(heappop(h)[1])
        
        return res
