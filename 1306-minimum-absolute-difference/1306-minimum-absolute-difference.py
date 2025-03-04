'''
- find the minimum abs difference
- return all pair of num that have the same minimum abs difference, the pair must be ascending

have a min variable to keep track of the diff
- curMin < min: find a smaller min, replace with the current min, save the numbers
- currMin = min: add the pair, add this pair of num to
- sort ascednding at the end when find out all pair has 

question: only consider 2 number next to each other? -> yes

brute force time O(n^2) have 2 pointer 
'''

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        res = []
        for i in range(0, len(arr)-1):
            currDiff = abs(arr[i] - arr[i+1])
            if currDiff < minDiff:
                minDiff = currDiff
                res = [[arr[i], arr[i+1]]]
            elif currDiff == minDiff:
                res.append([arr[i], arr[i+1]])
        return res


        