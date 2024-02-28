class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        curr = 0
        for weight in w:
            curr += weight
            self.arr.append(curr)

    def pickIndex(self) -> int:
        min_val = 1
        max_val = self.arr[-1]
        pick = randint(min_val, max_val)
        i = 0
        j = len(self.arr)
        while i < j:
            mid = (i+j)//2
            if self.arr[mid] < pick:
                i = mid + 1
            else:
                j = mid
        return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()