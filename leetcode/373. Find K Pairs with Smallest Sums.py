from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        heappush(h, (nums1[0]+nums2[0], 0, 0))
        res = []
        seen = set()
        
        while len(res) != k and len(h) != 0:
            _, i, j = heappop(h)
            res.append([nums1[i], nums2[j]])
            
            if i < len(nums1)-1:
                if (i+1, j) not in seen:
                    seen.add((i+1, j))
                    heappush(h, (nums1[i+1]+nums2[j], i+1, j))
            if j < len(nums2)-1:
                if (i, j+1) not in seen:
                    seen.add((i, j+1))
                    heappush(h, (nums2[j+1]+nums1[i], i, j+1))
            
        return res
