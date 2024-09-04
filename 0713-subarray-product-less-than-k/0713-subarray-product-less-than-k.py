class Solution:
    '''
    idea:
    - find a matching start of the arrray with an ending number
    - the total number of the subsarray is the total subarray contain the ending number expanding the matching start 
    so that we can reduce the redundant 
    (nhóm số, nhóm từ dưới đi lên bắt đầu từ nums[end] lên phía trước array, số tổ hợp của subarray sẽ tính từ nums[end] với số trước nó và trải dài đến đầu array 
    - số  số subarray chính là khoảng cách từ nums[end] tới nums[start]

    [10,5,2,6]
     l
        r
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        product = 1
        count = 0
        
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k and start <= end:
                product /= nums[start]
                start += 1
            count += (end - start + 1) #update count when we find the correct range of num and after update the start pointer
        return count

        