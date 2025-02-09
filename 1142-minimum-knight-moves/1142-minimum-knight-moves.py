from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Directions the knight can move in: 8 possible moves
        delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
        
        # BFS function to find the minimum steps
        def bfs(start, target):
            visited = set()
            queue = deque([start])
            visited.add(start)
            steps = 0
            
            while queue:
                n = len(queue)
                for _ in range(n):
                    node = queue.popleft()
                    if node == target:
                        return steps
                    # Explore all 8 possible knight moves
                    for i in range(8):
                        r, c = node
                        new_r, new_c = r + delta_row[i], c + delta_col[i]
                        if (new_r, new_c) not in visited:
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c))
                steps += 1
            return -1  # unreachable target, but it won't happen in this problem

        # The BFS starts from (0, 0) and we want to find the shortest path to (x, y)
        return bfs((0, 0), (x, y))

        