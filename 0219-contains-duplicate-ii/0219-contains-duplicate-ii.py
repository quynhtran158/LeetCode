'''
can we find a pair of duplicate in the k size of window
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            #check if we are in the valid size of window:
            if right - left > k: #valid: <= k
                #remove the leftmost element in the window until the window is valid:
                window.remove(nums[left]) #left still 0
                #increase left by 1 index
                left += 1
            if nums[right] in window:
                return True
            #if not in window:
            window.add(nums[right])
        return False
        