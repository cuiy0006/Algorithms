class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            s1 = -heappop(h)
            s2 = -heappop(h)
            s = s1 - s2
            if s > 0:
                heappush(h, -s)
        
        if len(h) == 0:
            return 0
        return -heappop(h)
