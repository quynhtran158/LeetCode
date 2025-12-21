class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x #0,1
        
        start, end = 1, x
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            sq = mid * mid 

            if sq == x:
                return mid
            elif sq < x:
                ans = mid 
                start = mid + 1
            else:
                end = mid -1 
        return ans

        