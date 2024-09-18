class Solution:
    '''
    moi cai query se la 1 cai target
    co condition la sum, neu cai so nho nhat tim duoc = sum -> next query
    neu cai so nhỏ tìm duoc < query ->tiep tuc tim
    
    - have a count to keep track of the subsequence of each query
    - loop through all query to find the subsequence
    '''
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
      
        
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        answer = []
        for query in queries:
            l, r = 0, len(prefix_sum)-1
            count = 0
            
            while l <= r:
                mid = (l+r) //2
                if prefix_sum[mid] <= query:
                    count = mid + 1
                    l = mid + 1
                else:
                    r = mid -1
            answer.append(count)
        return answer