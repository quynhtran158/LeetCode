import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles) 
        for _ in range(k):
            x = heapq.heappop(piles)
            remove = x // 2
            heapq.heappush(piles, remove)
        sumNum = abs(sum(piles))
        return sumNum
        
        