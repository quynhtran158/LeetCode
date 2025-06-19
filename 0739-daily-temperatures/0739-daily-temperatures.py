'''
can be empty? -> no
all tempurature all integer? -> 
all positive? - yes

plan:
use stack to keep track day haventy found warm
intialize stack wiht zero , loop thru tempt list to check whether curetn temp í wearme than the last day in stack -> yes: calc #, no: add curr day to stack




'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            current = temperatures[i]
            while stack and current > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        
        return res