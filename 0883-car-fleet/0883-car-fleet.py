'''
is target always further than any position? no postion == target? -> yes
all position are unique? -> yes
always has car? if no how to return?

idea:
- sort the pair (position, speed) in reverse based on position -> the nearest to target will in the end of stack
- add the reversed pair to stack
- calc the est time to reach target
- check collision/car fleet:
    if the stack has >= car, check if the top car has smaller time (need less time to reach target) compare to the 2nd top car -> collisde appear (one land, behind car go faster, have to wait and go same speed with the car in the front)
    after checking, pop the top 
    if not collide, dont pop
    return the count of stack = number of car fleet
    
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair =  [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack=[]
        for (p,s) in pair:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
              