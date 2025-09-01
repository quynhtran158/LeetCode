'''
purpose of using monotonic decreasig stack is to keep track/calculate the day from the current warmer day to the previous day 

temp = [35,30,31, 34]
stack = [35, 30, 31] -> monotonic stack
want to add 34, we have to pop 30 and 31 to make sure it is decreasing.

by poping 31, 30 out we can also calculate the gap between these day> for 31: 3(34)- 2(31)

for 30: 3(34)-1(30)

the index of 30 31 will be taken by popin out from the stack, since in the stack we will store the input of that number. we store index instead of the value 


'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic stack keep track of warmmer temp, make sure the temp decreasing 
        stack = [] #extra memory
        #create a array to track waiting day to get to warmemrday 
        ans = [0] * len(temperatures) #cannot find warmer day after, return 0
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: #empurature[stack[-1]] current smallest temp, compare to maintain the monotonic stack
                #when find the warmer day, we pop the smaller temp out before adding the larger temp
                #index in top of stack is the smallest of the stack
                prevDayIndex = stack.pop()
                #calc the waiting day by taking current day - the prev day 
                ans[prevDayIndex] = i - prevDayIndex
                #keep popping the smaller index (day) until current i is the next index in the monotonic stack, then append i to stack to main tain the order
            stack.append(i)
        return ans
        