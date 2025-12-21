'''
return the value at timestamp <= current get timestamp -> bisect_left
value as tuple (val, TS) -> when check TS check second component from the tuple



'''
from bisect import bisect_right
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        #get key, then check the TS which <= currTS at the tiem get, then return the val
        if key not in self.d:
            return ""
        valueList = self.d.get(key)
        idx = bisect_right(valueList, (timestamp,"{")) #find the earliest larger curr search TS -> the right before is the answer
        if idx == 0: #ALL timestamps in the list are > curr search TS
            return ""
        return valueList[idx-1][1]
 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)