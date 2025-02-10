from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            x, y = point
            distance = (x**2 + y**2) #just math, learn from heart the formula :x
            heappush(heap,(distance,point))
        
        for _ in range(k):
            _, point = heappop(heap)
            res.append(point)
        return res