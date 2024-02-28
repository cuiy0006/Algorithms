class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            i = 0
            for _ in range(days):
                curr = cap
                while i < len(weights) and curr >= weights[i]:
                    curr -= weights[i]
                    i += 1
            return i == len(weights)

        i = 0
        j = sum(weights)
        while i < j:
            cap = (i+j)//2
            if can_ship(cap):
                j = cap
            else:
                i = cap + 1
        if can_ship(i):
            return i
        else:
            return i + 1
