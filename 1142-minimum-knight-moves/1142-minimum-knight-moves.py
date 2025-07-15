from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def getNeighbor(node):
            deltaRow = [-2, -2, -1, 1, 2, 2, 1 , -1] 
            deltaCol = [-1, 1, 2, 2, 1 ,-1, -2, -2] 
            res = []
            row, col = node
            for i in range(len(deltaRow)):
                nr = row + deltaRow[i]
                nc = col + deltaCol[i]
                res.append((nr, nc))
            return res
        def bfs(root):
            q = deque([root])
            visited = {root}
            step = 0
            
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node == (x,y):
                        return step
                    for neighbor in getNeighbor(node):
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)
                step += 1
            return step
        return bfs((0,0))

        