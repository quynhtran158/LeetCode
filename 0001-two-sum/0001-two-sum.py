class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using dictionary
        dict = {}
        
        #store the index and val in the dict -> key: val
        for i, val in enumerate(nums):
            diff = target - val
            if diff in dict:
                return [i, dict[diff]]
            else: 
                dict[val] = i
           
        return None
        #find the other number which sum up to the target

        