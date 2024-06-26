class Solution:
    """
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
                   0 1 
                     i j
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1  # Initialize count to 1 for the first element
        i = 0  # Initialize i to 0 to start from the first element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # Compare current element with the last unique element
                i += 1  # Move to the next position for the unique element
                nums[i] = nums[j]  # Update the position with the current unique element
                count += 1  # Increment count of unique elements
        
        return count  # Return the number of unique elements

            
