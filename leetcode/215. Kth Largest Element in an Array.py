from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = []
        for num in nums:
            if len(s) == k:
                if s[0] < num:
                    heappop(s)
                    heappush(s, num)
            else:
                heappush(s, num)
        return s[0]
