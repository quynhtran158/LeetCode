class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #to check if the grid is empty
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:

            #why popleft()?
                # use popleft in queue to make sure that we remove the left most element which is FIFO. Popleft will remove the element from the front of the queue, and make sure that we are exploring th closest unvisited neighbor first before moving to more distant ones 
            #why do we have to remove the element?
                # to make sure that the cel (r, c) visited is removed so that we don't re-vist that cell

                row, col = q.popleft()
                directions = [[1, 0] , [-1, 0], [0, 1], [0, -1]]
                            # down up right left 
            # declare the directions array with pairs of nums which are dr and dc (in the for loop below) 

                for dc, dr in directions:
                    r, c = row + dr, col + dc
            # if nay check dieu kien xem sau khi dich len xuong trai phai thi cai r hoac c co con nam trong grid hay khong
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1" and 
                        (r, c) not in visit):

                        q.append((r, c))
                        visit.add((r, c))
 #iterate through each row and column               
        for r in range(rows):
            for c in range(cols):
                # "1 " la string vi de bai initialize string
                # neu gap phai tat ca so 1 ma chua tung visit (va sau do gap so 0) thi increment num of islands ++ 
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands