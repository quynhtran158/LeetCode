'''
identify the col not sorted -> check 1st char for all row -> m x n time?
when see unsorted -> delete, but how to delete the whole col? => hashmap: key is col number, check 
- check order: convert char to ascii then compare -> not sorted remove key 




'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        
        for col in range(len(strs[0])):
            for row in range(len(strs)-1):
                if strs[row][col] > strs[row+1][col]:
                    ans += 1
                    break
        return ans
                
            
        