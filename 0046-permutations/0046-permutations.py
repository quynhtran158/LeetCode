'''
                               []
                (1,2,3).    (1,2,3).   (1,2,3)
            [1]               [2].          [3]
           (2,3)             (1,3).        (1,2)
        [1,2]. [1,3].      [2,1]. [2,3].  [3,1].  [3,2]
        (3).     (2).      (3).    (1).     (2).    (1)
    [1,2,3].    [1,3,2].   [2,1,3]. [2,3,1].  [3,1,1]. [3,2,1]


                             []
                (1,1.,3).    (1,1.,3).                  (1,1.,3)
            [1]               [1.].                       [3]
           (1.,3)             (1,3).                     (1,1.)
        [1,1.]. [1,3].      [1.,1]. [1.,3].         [3,1].  [3,2]
        (3).     (2).      (3).    (1).              (2).    (1)
    [1,1.,3].    [1,3,1.].   [1.,1,3]. [1.,3,1].  [3,1,1]. [3,2,1]

-startIndex: the index of current numeber using to create permutation from the list
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def dfs(startIndex):
            #based case
            if startIndex == len(nums):
                res.append(path[:])
                return 
            for i, num in enumerate(nums):
                if used[i]: #true, alr used
                    continue
                path.append(num)
                used[i] = True
                dfs(startIndex+1)
                path.pop()
                used[i] = False
        dfs(0)
        return res
        


        