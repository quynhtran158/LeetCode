'''
Q - Nov 14

is the 10s count from the 1st time appear/print or from the lastest time? -> from first time print
hashmap: key:val - message:earliest avail time (curr time + 10s)
how to update the time?


'''
class Logger:

    def __init__(self):
        self.mapping = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mapping:
            self.mapping[message ] = timestamp
            return True
        #time sau so với time trước nếu < 10 thì false
        else:
            if timestamp < self.mapping[message] + 10:
                return False
            else: 
                self.mapping[message ] = timestamp
                return True
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)