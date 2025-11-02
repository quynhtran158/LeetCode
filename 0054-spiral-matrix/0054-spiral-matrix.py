'''
direction: right, down, left, up (clockwise)

dirs = [(0,1), (-1,0), (1, 0), (0,-1)]
keep moving: topRow <= botRow and leftCol <= rightCol

move left to right: keep the row, move the col 
move down: keep the col, move the row 
move up: keep the col, move the row 
move left: keep the row, move the col




'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        topRow = 0 
        botRow = len(matrix) - 1 
        leftCol = 0
        rightCol = len(matrix[0]) - 1
        res = []

        while topRow <= botRow and leftCol <= rightCol:
        #move right
            for i in range(leftCol, rightCol + 1):
                res.append(matrix[topRow][i])
            topRow += 1

            #move donw
            if leftCol <= rightCol:
                for i in range(topRow, botRow + 1):
                    res.append(matrix[i][rightCol])
                rightCol -= 1

            #move left
            if topRow <= botRow:
                for i in range(rightCol, leftCol -1, -1):
                    res.append(matrix[botRow][i])
                botRow -= 1

            #move up
            if leftCol <= rightCol:
                for i in range(botRow, topRow -1, -1):
                    res.append(matrix[i][leftCol])
                leftCol += 1

        return res

'''
def spiral(matrix):
    direction = ['R', 'D', 'L', 'U']
    visited = set()
    m = len(matrix)
    n = len(matrix[0])
    ans = []
    row, col = 0, 0
    d = 0 # current direction

    while len(ans) < m*n:
        # add curr into ans
        ans.append(matrix[row][col])
        visited.add((row, col))

        if direction[d] == 'R':
            # turn 
            #   col == n-1
            #   matrix[row][col+1] in visited
            if col == n-1 or (row, col+1) in visited:
                row += 1
                d = (d+1) % 4
            else:
                # keep R
                col += 1
        elif direction[d] == 'D':
            # turn
            if row == m-1 or (row+1, col) in visited:
                col -= 1
                d = (d+1) % 4
            else:
                # keep D
                row += 1
        elif direction[d] == 'L':
            if col == 0 or (row, col-1) in visited:
                row -= 1
                d = (d+1) % 4
            else:
                # keep L
                col -= 1
        else:
            if row == 0 or (row-1, col) in visited:
                col += 1
                d = (d+1) % 4
            else:
                # keep U
                row -= 1
    
    return ans


'''
        