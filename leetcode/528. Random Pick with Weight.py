from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.acc_w = []
        self.sum_w = 0
        
        for weight in w:
            self.sum_w += weight
            self.acc_w.append(self.sum_w)

    def pickIndex(self) -> int:
        target = randint(1, self.sum_w)
        i = 0
        j = len(self.acc_w)
        
        while i < j:
            mid = (i + j) // 2
            if self.acc_w[mid] == target:
                return mid
            elif self.acc_w[mid] > target:
                j = mid
            else:
                i = mid + 1
        return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
