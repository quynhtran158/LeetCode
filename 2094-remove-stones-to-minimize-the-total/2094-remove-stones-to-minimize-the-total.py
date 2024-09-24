import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        total = 0
        
        for _ in range(k):
            curr = heapq.heappop(piles)
            if -curr % 2 != 0:
                curr = (-curr // 2) + 1
                heapq.heappush(piles, -curr)
            else:
                curr = -curr // 2 
                heapq.heappush(piles, -curr)
        for pile in piles:
            total += -pile
        return total
            


        