from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n
        
        sortedStart = sorted((start, idx) for idx, (start,_) in enumerate(intervals)) #tuple (start, original index )
        for idx, (_, end) in enumerate(intervals):
            position = bisect_left(sortedStart,(end, float("-inf"))) #sortedStart is tuple, compare tuple vs tuple
            if position < n: #in case the current start larger than all starts
                ans[idx] = sortedStart[position][1] #to find the index of the start interval found
        return ans




        