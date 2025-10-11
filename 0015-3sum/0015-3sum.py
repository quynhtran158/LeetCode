'''
plan: 
-4,-1,-1,0,1,2
       s
         l
            r


plan: 
sort array
- start at index 0 
- left = start + 1
- right at the end of array 
move left and right to find the triplet that can sum to 0 
if currSum < 0 move left += 1, currSum > 0, move right += 1

then start with new start

TC: O(n)
SP: O(1)

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for start in range(len(nums)-2):
            left = start + 1
            right = len(nums)-1

            if nums[start] > 0:
                break
            #prevent duplpicate for first element
            if start > 0 and nums[start] == nums[start-1]:
                continue

            while left < right:
                currSum = nums[start] + nums[left] + nums[right]
                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    res.append([nums[start], nums[left], nums[right]])
                    #keep moving left, right to find the next number with same start
                    left += 1 
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        #if dup, skip the current
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        #if dup, skip the curretn
                        right -= 1
        return res
