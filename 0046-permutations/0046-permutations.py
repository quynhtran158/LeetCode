class Solution:
    '''
    - dfs, backtracking 
    swap the number position, no duplicate number in the permutation
    have a bool list used to track either the numebr is used or not
    
    state space tree
                            []
                /.           |.      \
            1.              2.        3
         /.  \.          /.  \     /.   \
        2.     3        1.    3.   1.    2
       /.       \.   /.       \.   /.     \
       3.        2.  3.        1

      1,2,3.   1,3,2  
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path =[]
        used = [False] * len(nums)

        def dfs(start):
            if start == len(nums):
                res.append(path[:])
                return
            
            for i, num in enumerate(nums):
                #prunning invalid posibility
                if used[i]:
                    continue
                path.append(num)
                used[i] = True
                dfs(start+1)
                path.pop() #backtrack
                used[i] = False #pop num out so False
        dfs(0)
        return res

       