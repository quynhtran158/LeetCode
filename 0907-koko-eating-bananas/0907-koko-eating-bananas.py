'''
If Koko eats too slowly (small k), she won’t finish on time → not feasible.

If Koko eats fast enough (large k), she will finish within h hours → feasible.

As k increases, it only becomes easier for her to finish.
→ The relationship between k and “can finish?” is monotonic.

This monotonic property lets us apply binary search:find the smallest k such that Koko can finish all bananas within h hours.

If k is too small, she needs more than h hours → ❌ not feasible.

If k is big enough, she can finish within h hours → ✅ feasible.


finding the speed k/hour (number of banana need to eat per 1 hour) need to eat all pile in time

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k): #this is feasible function: to dèin whter koko cn finish all piles at speed k
            totalHours = sum((pilesize + k - 1) // k for pilesize in piles)
            #totalHours = ceil(float(p)/k) #này để tính nếu mà còn leftover trong pile, kiểu ăn 4 trái trong 1h àm pile có 6 trái -> 1.05 -> 2 tiếng ăn hết hay k vẫn count as full hour
            return totalHours <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canFinish(mid): #this is feasible function: to dèin whter koko cn finish all piles at speed k
                right = mid #keep mid as potential answer
            else:
                left = mid + 1
        return left #where left = right