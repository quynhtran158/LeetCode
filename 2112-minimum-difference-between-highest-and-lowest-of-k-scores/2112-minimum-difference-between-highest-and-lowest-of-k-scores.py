'''
- can i assume that k number will always larger or equal to 1? -> yes
- is there a case where the nums is the empty array? -> no
- what is the maximum length of the array nums? -> 1000
- is the number in array nums sorted? -> no
- is the number in array nums all positive? -> yes

plan:
- have a window with the length of k
- sliding the k-length window to find the 2 highest and the smallest nums out of k-number 
- calculate those 2 number and return the mnimum 
- sort array -> min is the first element, max is the kth element in the window -> O(nlogn) time

nums= [1,2,5,9,7,8,3] 

'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float('inf')

        for i in range(len(nums)-k+1): #to make sure we dont go out of bound
            curr_diff = nums[k+i-1] - nums[i]
            min_diff = min(curr_diff, min_diff)
        return min_diff
        