import heapq
class Solution:
    '''
    - the arr has all same numbers?
    - the arr has duplicate? 

    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        sorted =[1,2,2,3,3,4,5,5,6] k = 4

    Output: 4
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for _ in range(k):
            ans = heapq.heappop(nums)
        return -ans

        