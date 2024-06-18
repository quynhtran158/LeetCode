class Solution:
    '''
    O(n^2) naive approach, 2 for loops

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0 #two pointer to count the n number
        cSum = 0 #current sum
        mSum = float("-inf")
        #while i in range(len(nums)) and i < (len(nums) -2):  
        for i in range(len(nums) -k +1) :
            cSum = 0                                              # +1 la de include that index
            #for j in range(i, k+1): k+1 la spanding tu i xong lay THEM k index 01234 trong khi minh lay 0123 th
            for j in range(i, i+k): #i+k la inclusive index k, tai i tang nen upate cai boundary cua k
                cSum += nums[j]
            mSum = max(cSum, mSum)
        return mSum / k
        '''
    #sliding window
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wSum, mSum = 0, float('-inf')
        for i in range(k):
            wSum += nums[i]
            print("wSum",wSum)
        mSum = max(mSum, wSum)
        print ("mSum",mSum)
        print("done 1 loop")
        for j in range(k, len(nums)): 
            #because we alr have the first window len of k value in the first loop, we start with index k (which is not correct in term of index, but easy for us to calculate the value when we sliding the window or in differentway, we udpate the window value)
            #if we start at k = 4, which is index 3. However, we dont need to start at k - 1 which is the real index 3, because we just get start at index 0 in the first loop alr, so in this for loop we want to update the window which will slide 1 index before (which is the 4th element, the index 3)
            #for range() function, it doesnt include the ending range so with k = 4, it will perfectly consider the 4th element, the index 3
            wSum = wSum - nums[j-k] + nums[j]
            print("wSum",wSum)
            mSum = max(mSum, wSum)
            print ("mSum",mSum)
        print("done 2 loop")
        return mSum / k