class Solution:
    '''
    0 1 2 3 4 5
    5 0 1 2 3 4
    if left < right -> no rotation -> check left and left + 1
    if left > right -> have some rotation => need to find the order turning point to the right of the mid

    '''
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        

        while left < right:
            if nums[left] < nums[right]: #sorted array, no rotation:
                return nums[left]
            mid = (left + right) // 2
             #nums[left] > nums[right] -> have rotation, need to find the order turning point in the right of mid
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:  #find the turning point to the left of mid
                right = mid
            else:
                return nums[right]
        return nums[left]    
            


