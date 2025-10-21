from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRow, numCol = len(grid), len(grid[0])

        def get_neighbors(coord):
            r, c = coord
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            res = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # check boundary validity
                if 0 <= nr < numRow and 0 <= nc < numCol:
                    res.append((nr, nc))
            return res

        def bfs(start):
            q = deque([start])
            r, c = start
            grid[r][c] = "0"  # mark as visited
            while q:
                node = q.popleft()
                for nr, nc in get_neighbors(node):
                    if grid[nr][nc] == "1":  # found land
                        grid[nr][nc] = "0"  # mark visited
                        q.append((nr, nc))

        count = 0
        for r in range(numRow):
            for c in range(numCol):
                if grid[r][c] == "1":  # new island
                    count += 1
                    bfs((r, c))
        return count
