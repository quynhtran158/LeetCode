'''
start with the edge: top and left for pacific, bottom and right col for left -> the ocean boundary
- cell on row 0, or col 0 reach Pacifi
- cell on row m-1 (last row) or col n-1 (the right last col) reach atlantic
- have 2 queue: 1 queue for pacific and 1 queue for atlantic 
- if the neighbor of edge has higher or equal amount, add to the queue, if not meet condition skip 
- after find all coord reach pacific and atlantic, find intersection. the coord that in both queue will be the answer 
- move if water in next cell > current cell (h[x][y] > h[i][j])


not thinking reverse then Total Time = (Number of cells to check) × (Work done per cell)
Total Time = (m * n) × (O(m * n) for the Pacific search + O(m * n) for the Atlantic search)
Total Time = (m * n) × O(m * n)
Total Time = O(m² * n²)
'''
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue, visited):
            while queue:
                levelSize = len(queue)
                for _ in range(levelSize):
                    currRow, currCol = queue.popleft()
                    #check all adjacent right, left up down 
                    directions = [[0,1],[0,-1], [-1,0], [1,0]]
                    for dr, dc in directions:
                        nextRow, nextCol = currRow + dr, currCol + dc
                        #check if next cell is valid, next cell >= curr cell
                        if (0<= nextRow < numRows and 
                            0<= nextCol < numCols and 
                            (nextRow, nextCol) not in visited and 
                            heights[nextRow][nextCol] >= heights[currRow][currCol]):
                            visited.add((nextRow, nextCol))
                            queue.append((nextRow, nextCol))
        
        numRows, numCols = len(heights), len(heights[0])
        visP = set()
        visA = set()
        queueP = deque()
        queueA = deque()

        for row in range(numRows):
            for col in range(numCols):
                #pacific: col 0, row 0
                if row == 0 or col == 0:
                   visP.add((row, col))
                   queueP.append((row, col))
                #atlantic: bottom edge, right edge 
                if row == numRows - 1 or col == numCols - 1:
                   visA.add((row, col))
                   queueA.append((row, col))
        #find all cell reachable from ocean
        bfs(queueA, visA)
        bfs(queueP, visP)

        res = []
        for row in range(numRows):
            for col in range(numCols):
                if (row, col) in visA and (row, col) in visP:
                    res.append([row,col])
        return res






      

    

        