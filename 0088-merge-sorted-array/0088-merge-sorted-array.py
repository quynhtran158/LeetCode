'''
plan:
- arrange the number at the back of the nums1, then after sorted the array then return the reverse nums1
- have 2 pointer left and right, left to iterating through nums1 array, right interating thourgh nums2 array
- compare the nums1[left] and nums2[right] then put the number in the back of array nums1
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n-1
        insert_ind = m + n - 1
        #keep iterating until we reach the start of both array
        #  no need to check the edge case bc the 2P can handle the empty case
        # if m == 0 or n == 0:
        #     if m == 0:
        #         nums1[insert_ind] = nums1[left]
        #         left -= 1
        #     else:
        #         nums1[insert_ind] = nums2[right]
        #         right -= 1
        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[insert_ind] = nums1[left]
                left -= 1
                
            else:
                 nums1[insert_ind] = nums2[right]
                 right -= 1
            insert_ind -= 1

        # Copy remaining elements from nums2 to nums1. Even though nums1 is empty but the length of nums1 is still availble. if nums1 is empty then left is -1 then the main code above wont be execute, so it wil jump directly to the code bellow here:
        while right >= 0:
            nums1[insert_ind] = nums2[right]
            right -= 1
            insert_ind -= 1

        return nums1   

            