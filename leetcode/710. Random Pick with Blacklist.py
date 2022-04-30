from random import randint

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.dic = {} # blacklist num -> num
        blacklist = set(blacklist)
        
        i = n-m
        for black_num in blacklist:
            if black_num >= n-m:
                continue
            while i < n and i in blacklist:
                i += 1
            self.dic[black_num] = i
            i += 1
        self.limit = n-m-1

    def pick(self) -> int:
        num = randint(0, self.limit)
        if num in self.dic:
            return self.dic[num]
        else:
            return num


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
