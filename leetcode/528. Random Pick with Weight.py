from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.sum_lst = []
        
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.sum_lst.append(curr_sum)
        

    def pickIndex(self) -> int:
        weight_sum = self.sum_lst[-1]
        target = randint(0, weight_sum - 1)
        
        for i, weight_sum in enumerate(self.sum_lst):
            if target < weight_sum:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
