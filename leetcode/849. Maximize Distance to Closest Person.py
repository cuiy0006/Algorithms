class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_d = -1
        last = None
        for i, seat in enumerate(seats):
            if seat == 1:
                if last is None:
                    last = i
                    max_d = i
                else:
                    d = (i - last) // 2
                    max_d = max(max_d, d)
                    last = i
        
        max_d = max(max_d, len(seats)-1-last)
        return max_d
