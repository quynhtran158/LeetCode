class Solution:
    '''
    if the height of 2 lines are different, the area of water depends on the shorter line

    area = height x width
    height = the shorter line
    width = distand between 2 lines

    what if 2 line has same height? which pointer to move? either is fine, since the width is reduced 
    by one
    example:
        8
        8    6        7
        8    6        7
    1   8    6    2   7
        l
            r
                    
    move the pointer in the shorter line 

    '''
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxArea = 0
        while l < r:
            width = r - l
            currHeight = min(height[r], height[l])
            maxArea = max(maxArea, width * currHeight)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea

        