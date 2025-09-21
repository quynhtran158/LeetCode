'''
- all english alphabet? yes
- all non-numeric char? yes
- low/upper case? doesnt matter
- punctuation? yes, "," and "." -> treat them like normal letter?
- symbol? no
- whitespace? no
- s wil be non-empty? yes
- will the numRow can store all char in s? if not how to return? -> return s

edge case:
- when numRow = 1 -> no zigzag -> return s?
- numRow = str len -> return s itself since each row is each char

plan:
- zigzag pattern appear when 1 full vertical happend and diagonal cycle
- start from top row, iterate each char in s, place in row 
- if at top/bottom row, flipp/change the direction then move to the next row 

- 1 cycle is go down and go up diagonally
- character per cycle: numRow (char in 1 col) + numRow - 2 (the diagonal) = 2 * (numRow - 1)
- number of cycle for str len n: n/number of char per cycle = n/[2 * (numRow - 1)]
- how wide we go: numRow - 1 per 1 cycle
- total column needed: numCol per 1 cycle * total cycle = (numRow - 1) * n/[2 * (numRow - 1)]

how to traverse the matrix as zigzag order
- go from top to bottom in a col, currCol remain the same
- go diagonally, move 1 cell up and to the right and increment the currCol by 1, decrea currRow by 1 (di xeo thi col tang, row giam) until reach currRow = 0
=> repeat this until traverse all n 




'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRow >= len(s): return s

        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if 0 < r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]

        return res