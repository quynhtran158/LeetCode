class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRow, numCol = len(grid), len(grid[0])
        def get_neighbor(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0 , -1]
            res = []
        
            for i in range(len(delta_col)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < numRow and 0 <= neighbor_col < numCol:
                    res.append((neighbor_row, neighbor_col))
            return res
        
        def bfs(start):
            q = deque([start])
            r, c = start
            grid[r][c] = "0" #mark = 0 as visited, change from 1 to 0
            while q:
                node = q.popleft()
                for neighbor in get_neighbor(node):
                    nr, nc = neighbor
                    if grid[nr][nc] == "0":
                        continue
                    q.append(neighbor)
                    grid[nr][nc] = "0"
        count = 0
        for r in range(numRow):
            for c in range(numCol):
                if grid[r][c] == "0":
                    continue
                bfs((r,c))
                count += 1
        return count
                    
        