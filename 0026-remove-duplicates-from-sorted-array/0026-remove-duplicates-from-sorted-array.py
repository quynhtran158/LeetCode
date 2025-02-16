class Solution:
    '''

    question:
- empty array?

case:
- all duplicate
- all non dupplicate
- mixed 

plan:
- have 2 pointers: left pointer to indicate the index of non-duplicate number
and right pointer to find the non-duplicate number

[0, 1, 1, 1, 1, 2, 2].
    l
                r
                
key:
only update left pointer when find the non-duplicate number (arr[left] != arr[right)
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] > nums[j-1]:
                nums[i] = nums[j]
                i += 1
        return i