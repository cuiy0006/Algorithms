class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.dic = defaultdict(int)
        for num in nums:
            self.dic[num] += 1
        

    def showFirstUnique(self) -> int:
        while len(self.q) != 0 and self.dic[self.q[0]] > 1:
            self.q.popleft()
            
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]
    

    def add(self, value: int) -> None:
        self.dic[value] += 1
        if self.dic[value] <= 1:
            self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
