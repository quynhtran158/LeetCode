class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        boolean = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandy:
                boolean[i] = True
        return boolean
        