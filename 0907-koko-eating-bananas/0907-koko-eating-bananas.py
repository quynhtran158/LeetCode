class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(num):
            hours = 0
            for pile in piles:
                hours += ceil(pile/num)
            return hours <= h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1
        
        return right