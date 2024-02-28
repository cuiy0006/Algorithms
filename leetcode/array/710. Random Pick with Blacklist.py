class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.dic = {}
        j = n-1
        size = n - len(blacklist)
        blacklist.sort()
        blacklist_set = set(blacklist)
        for num in blacklist:
            if num > size - 1:
                break
            while j in blacklist_set:
                j -= 1
            self.dic[num] = j
            j -= 1
        self.size = size

    def pick(self) -> int:
        num = randint(0, self.size-1)
        if num in self.dic:
            return self.dic[num]
        else:
            return num


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()