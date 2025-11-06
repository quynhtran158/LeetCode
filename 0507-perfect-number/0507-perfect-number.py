'''
the divisor and result of divident / divisor comes as pair then it will be repeated

divident = 8
check to half of num -> square root 
divisor
1 - 8
2 - 4
3 x
4 - 2 (repated)



'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False #1 is not perfect num,is prime num

        currSum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                currSum += i
                if i != (num // i): #add the other num in pair only when i is the divisor
                    currSum += (num // i)
        return currSum == num