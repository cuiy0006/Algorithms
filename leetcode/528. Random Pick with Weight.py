import random

class Solution:

    def __init__(self, w: List[int]):
        self.ranges = []
        curr = 0
        for weight in w:
            curr += weight
            self.ranges.append(curr)

        self.total = curr
        

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        
        i = 0
        j = len(self.ranges)
        while i < j:
            mid = (i + j) // 2
            if self.ranges[mid] == target:
                break
            elif self.ranges[mid] > target:
                j = mid
            else:
                i = mid + 1

        if self.ranges[mid] < target:
            return mid + 1
        else:
            return mid

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
