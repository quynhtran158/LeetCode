# '''
# assumpotion:
# - will we have empty array?
# - all unique num appear once -> return all regardless otth the kth 
# - single element -> auto return regardless of the kth
# - many nums have same frequency, the number larger then the kth -> return any numbers that meet the reuqirement of kth

# '''

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequency = {}
#         if len(nums) == k:

#         for num in nums:
#             if num not in frequency:
#                 frequency[num] = 1
#             frequency[num] += 1
#         #convert the map into array with the order base on the frequency?
#         #convert the arr to heap?
#         #

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        cnt = Counter(nums) #this will count each num with its frequency as a hashmap
        heap = []

        for num, freq in cnt.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [num for freq, num in heap]


