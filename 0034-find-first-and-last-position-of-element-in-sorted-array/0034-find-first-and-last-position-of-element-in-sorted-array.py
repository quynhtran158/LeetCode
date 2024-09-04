class Solution:
    ''' 
    edge case:
    - day so giong nhau 
    0 6 3
    5,6,7,7,8,8,10
    s
      m
          e
    mid < target -> end = mid
    
    5,6,6,6,7,7,7,8,8,10.   0-9 4
    s
        m
            e
    1 
    2
    3

    tim duoc mid tai cai so target, shrink cai s en lai mid-1, mid+1 roi expand dan ra de tim duoc het cac so
    while nums[e] == target and nums[s] == target: -> can biet cai nao out cai target range
        e + 1
        s - 1
    khi nao e hoac s != target thi return cai s+1, e-1

    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
    
    # First, find the target element using binary search
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                # Found the target, now expand to find the range
                left, right = mid, mid
                # Expand to the left
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                # Expand to the right
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # If target is not found
        return [-1, -1]