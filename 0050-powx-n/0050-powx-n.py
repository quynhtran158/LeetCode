'''
I’m using Exponentiation by Squaring. Instead of multiplying x repeatedly, I square x each iteration — which effectively builds powers of 2 (x², x⁴, x⁸...). When n is odd, I multiply res by the current x to accumulate the remaining exponent. This reduces time complexity from O(n) to O(log n).

x^4 = (x^2)^4
x^5 = x * x^4 = x *(x^2)^2

n = 5 -> in binary 8 4 2 1 -> 7 = 0111 
x^5 = x^1 * x^2 * x^4
=> if n is odd its last bit is 1
remove the extra x (x^5 = x * x^4), store in res 


'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                res *= x   # save that extra x
                n -= 1     # make exponent even
             # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2
        
        return res