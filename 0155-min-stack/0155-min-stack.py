'''
are the function call on non-empty? if empty what to return? null? -1?
2 stacks: 1 for the operation, 1 to track the minimum
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) #override the val with min
        self.minStack.append(val)
        

    def pop(self) -> None:
        #have to pop both stacks bc what if the val of the stack if the min (val) of the minStack?
        self.stack.pop()
        # if self.minStack[-1] == self.stack[-1]:
        self.minStack.pop() 

    def top(self) -> int:
        #alway call on non-empty
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
