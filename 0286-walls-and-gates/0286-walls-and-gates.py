class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        directRow = [-1, 0, 1, 0]
        directCol = [0, 1, 0, -1]
        q = deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            row, col = q.popleft()
            for i in range(len(directRow)):
                nr = row + directRow[i]
                nc = col + directCol[i]

                if 0 <= nr < len(rooms) and 0 <= nc < len(rooms[0]):
                    if rooms[nr][nc] == INF:
                        rooms[nr][nc] = rooms[row][col] + 1
                        q.append((nr, nc))
        return rooms
                    

