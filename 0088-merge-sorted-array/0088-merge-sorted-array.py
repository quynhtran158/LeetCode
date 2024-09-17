class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
                     l.    
                           ind.       
                                                    r
        do i need to increase the length of the nums1 by myself?
        can nums1 or nums2 be empty? can both arr be empty?

        """
        l, r, index = m -1, n-1, (m+n)-1
        while  l >= 0 and r >= 0:
            if nums2[r] >= nums1[l]:
                nums1[index] = nums2[r]
                r -= 1
            #move right down bc we add it to the ind, need to find another one
            else:
                nums1[index] = nums1[l]
                l -= 1
            index -= 1
           
        # If there are remaining elements in nums2, copy them into nums1
        #here, where we visted all of 
        while r >= 0:
            nums1[index] = nums2[r]
            r -= 1
            index -= 1
        return nums1

        