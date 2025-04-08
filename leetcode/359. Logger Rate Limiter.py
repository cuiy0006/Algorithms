class Logger:

    def __init__(self):
        self.seen = set()
        self.q = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while len(self.q) != 0 and self.q[0][0]+10 <= timestamp:
            ts, msg = self.q.popleft()
            self.seen.remove(msg)
        if message in self.seen:
            return False
        self.q.append((timestamp, message))
        self.seen.add(message)
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
