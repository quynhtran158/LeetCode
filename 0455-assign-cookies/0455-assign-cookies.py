class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        left, right = 0, 0
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                right += 1
                left += 1
                count += 1
                
            #if the size and the greedy factor of the child not match, we move to the next cookie
            else: right += 1
        return count