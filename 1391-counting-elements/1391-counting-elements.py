class Solution:
    def countElements(self, arr: List[int]) -> int:
        '''
        add array value into a hash map with key is the num, val is freq, 
        check at curr x if we have x+ 1, we decrease the freq of x
        
        '''
        hashset = set(arr)
        count = 0
        for num in arr:
            if num+1 in hashset:
                count += 1
        return count