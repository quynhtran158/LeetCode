class Solution:
    '''
   no need to check whether the array is rotated
    check arr[0] and arr[-1]
    if arr[0] > arr[-1] -> rotated 
    compare with arr[-1] as target

    [40, 50, 10, 20, 30]
    l
                    r
    r < l => possibility r is the smallest, discard right to find the
    smallest in front of current r
    
    2 scenario < right and > right since all item are unique
    ''' 
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        ans = 0 #if the list is not rotated
        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= nums[-1]:
                ans = mid
                right = mid -1 #possibility having smaller in the front
            else:
                left = mid + 1
        return nums[ans]
        