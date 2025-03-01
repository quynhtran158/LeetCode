'''
track the smallest and the second biggest. if the biggest appear, return true
negative number? yes 
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        smallest = float('inf')
        second_biggest = float('inf')

        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_biggest:
                second_biggest = num
            else:
                return True
        return False

        