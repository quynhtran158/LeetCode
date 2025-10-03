class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
    as this is non-decreasing order 2 array
    - start at the back of both array to get biggest number of each array then merge/insert the number from the back of num1 by bigger to smaller order
    - use 3 pointer: 1 at the back of nums1
    1 at the back of nums2
    1 at the end of the actual number in nums1

the nums1 has extra 0 to fit both nums1 and nums2 len
    ex: 
     nums1 = [1,2,3,0,0,0]
                  1     1 
     nums2 = [2,5,6]
                  3

    time: O(n)
    space: O(1) since we merge in place 
        """
        left, right = m - 1, n -1 #pointer at the end of the arrays
        p = m + n - 1 #
        while right >=0:
            if left >= 0 and nums2[right] <= nums1[left]:
                nums1[p] = nums1[left]
                left -= 1
            else: #(left < 0) or (nums2[right] > nums1[left])
                #left < 0 but right >= 0 means reach the start of num1 but num2 didnt
                nums1[p] = nums2[right]
                right -= 1
            p -= 1
                
        return nums1



        