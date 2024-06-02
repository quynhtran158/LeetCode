class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #create an arrray with the len of array nums
        pref = 1 #the left most number of the first index number does not exist so we assign/assume that the pref of the 1st number in the array is 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i] #at this point, prefix is 1 and it's in the nums[0], nums[1] will have value of pref (1) x nums[0] -> so we just need to udpate pref to have the product
        post = 1 #after fill the prefix in the result array, we will multiple the pref with the postfix to get the final result
                #the right most postfix of the last num in array doesnt exist so we assume, assign it as 1 (same as pref)

        for i in range(len(nums) -1, -1, -1): #at this time we multiply the post with the current pref in the array so we have to start from the end. The code above means, start at the back, 1 index per step
            res[i] *= post 
            post *= nums[i]

        return res
