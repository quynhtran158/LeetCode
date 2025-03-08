from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRow, numCol = len(grid), len(grid[0])
    
        # Helper function to get valid neighboring cells
        def getNeighbor(coord):
            res = []
            r, c = coord
            deltaRow = [-1, 0, 1, 0]  # Up, Right, Down, Left
            deltaCol = [0, 1, 0, -1]
            for i in range(len(deltaRow)):
                neighborRow = r + deltaRow[i]
                neighborCol = c + deltaCol[i]
                if 0 <= neighborRow < numRow and 0 <= neighborCol < numCol:
                    res.append((neighborRow, neighborCol))
            return res
    
        def bfs(start_nodes):
            q = deque(start_nodes)  # Start with all initial rotten oranges
            minutes = 0
            fresh_count = sum(row.count(1) for row in grid)  # Count fresh oranges
            
            if fresh_count == 0:
                return 0  # No fresh oranges to rot
            
            while q and fresh_count > 0:
                level_size = len(q)  
                for _ in range(level_size):
                    node = q.popleft()
                    r, c = node
                    for neighbor in getNeighbor(node):
                        nr, nc = neighbor
                        if grid[nr][nc] != 1:  # Skip if not a fresh orange
                            continue
                        grid[nr][nc] = 2  # Rot the fresh orange
                        fresh_count -= 1
                        q.append(neighbor)
                minutes += 1  # Increment time after processing this level
            
            return minutes if fresh_count == 0 else -1
    
        # Find all initial rotten oranges as starting points
        rotten = []
        for r in range(numRow):
            for c in range(numCol):
                if grid[r][c] == 2:
                    rotten.append((r, c))
        return bfs(rotten)