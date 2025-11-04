'''
- identify pattern 10-char long return more than 1



'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, output = set(), set()

        for start in range((n - L + 1)): #the posible last index, +1 to slice right exclusive
            window = s[start:start+L]
            if window in seen:
                output.add(window)
            else:
                seen.add(window)
        return list(output)
