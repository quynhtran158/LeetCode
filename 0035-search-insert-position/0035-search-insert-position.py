class Solution:
    '''
    nums = [1,3,5,6], target = 2 7
            l
              mid
            r

    case: 
    target not in array:
    larger than existing num in arr
    

    [1,3,5,6] 7
              l 
           m
            r
    [1,3,5,6] 2 => 2 > 1 so the loop only break when condition l <= r is not working, in this case our current l is at index 1 which is the position we supposed to put 2 and it is the condition to break the while loop
    l 
    m
    r
    same to the case where target is smaller than the smallest existing num in the arr right will discard the right, which will go to -1 
    -> break the loop since r < l, and current l is 0 so that is also the index where we should put 0 in 

    [1,3,5,6] 0  
    l 
    m
    r          
       

    smaller than existing num in arr
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        # l = r and target != nums[mid]
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1 
        return l