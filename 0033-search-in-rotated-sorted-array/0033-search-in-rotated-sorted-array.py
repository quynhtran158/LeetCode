class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        # 1. Find the rotation index (smallest element)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left  # smallest element index
        
        # 2. Decide which half to search based on target
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            start, end = pivot, len(nums) - 1
        else:
            start, end = 0, pivot - 1
        
        # 3. Regular binary search
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
