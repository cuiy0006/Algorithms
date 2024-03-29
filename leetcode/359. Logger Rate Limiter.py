class Logger:

    def __init__(self):
        self.ts_to_msg = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.ts_to_msg:
            self.ts_to_msg[message] = timestamp
            return True
        else:
            if self.ts_to_msg[message] + 10 > timestamp:
                return False
            else:
                self.ts_to_msg[message] = timestamp
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
