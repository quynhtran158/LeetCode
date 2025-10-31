class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #interval tuple [start, end]
        #sort by the fisrt ele in tuple
        intervals.sort(key = lambda x: x[0]) 
        res = []
        res.append(intervals[0])
        
        for interval in intervals[1:]:
            startTime, endTime = interval
            #check the last interval in list (-1)
            #(1) take the end time
            #this conditiona take the starttime compare with end time to find the overlap 
            if startTime <= res[-1][1]:
                #take the later end time, update to the last (-1) interval
                #should span from start to latest end

                res[-1][1] = max(res[-1][1], endTime)
            else:
                res.append(interval)
        
        return res

