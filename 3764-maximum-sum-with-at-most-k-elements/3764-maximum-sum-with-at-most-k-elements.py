from typing import List
import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n, m = len(grid), len(grid[0])
        
        max_heap = []  
        for i in range(n):
            grid[i].sort(reverse=True)  # Sort row in descending order
            if limits[i] > 0 and grid[i]:  
                heapq.heappush(max_heap, (-grid[i][0], i, 0))  

        row_count = [0] * n  
        max_sum = 0

        while k > 0 and max_heap:
            val, row, col = heapq.heappop(max_heap)
            val = -val  
            
            max_sum += val
            row_count[row] += 1
            k -= 1
            
            if row_count[row] < limits[row] and col + 1 < len(grid[row]):
                heapq.heappush(max_heap, (-grid[row][col + 1], row, col + 1))

        return max_sum
