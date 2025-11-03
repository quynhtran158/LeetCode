'''
- hashMap key:val mess: time

'''

class Logger:

    def __init__(self):
        self.lastSeen= {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lastSeen or timestamp - self.lastSeen[message] >= 10:
            self.lastSeen[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)