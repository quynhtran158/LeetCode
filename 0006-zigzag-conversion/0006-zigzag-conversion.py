'''
- all english alphabet? yes
- all non-numeric char? yes
- low/upper case? 
- punctuation? yes, "," and "." -> treat them like normal letter?
- symbol? no
- whitespace? no
- s wil be non-empty? yes
- will the numRow can store all char in s? if not how to return?

edge case:
- when numRow = 1 -> no zigzag -> return s?

plan:
- zigzag pattern appear when 1 full vertical happend and diagonal cycle
- start from top row, iterate each char in s, place in row 
- if at top/bottom row, flipp/change the direction then move to the next row 


'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if 0 < r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]

        return res