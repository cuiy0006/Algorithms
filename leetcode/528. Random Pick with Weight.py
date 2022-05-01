from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.prefix = []
        for num in w:
            self.total += num
            self.prefix.append(self.total)


    def pickIndex(self) -> int:
        target = randint(1, self.total)
        
        i = 0
        j = len(self.prefix)-1
        while i < j:
            mid = (i+j) // 2
            if self.prefix[mid] >= target:
                j = mid
            else:
                i = mid + 1
        
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
