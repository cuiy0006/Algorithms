class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        while len(self.q) != 0 and self.q[0] + 3000 < t:
            self.q.popleft()
        self.q.append(t)
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
