class Solution:

    def __init__(self, m: int, n: int):
        self.end = m*n-1
        self.n = n
        self.m = m
        self.dic = {}

    def flip(self) -> List[int]:
        i = random.randint(0, self.end)
        if i in self.dic:
            idx = self.dic[i]
        else:
            idx = i
        replace = self.end
        while replace in self.dic:
            replace = self.dic[replace]
        self.dic[i] = replace
        self.end -= 1

        x = idx // self.n
        y = idx % self.n
        return [x, y]

    def reset(self) -> None:
        self.dic.clear()
        self.end = self.m*self.n-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
