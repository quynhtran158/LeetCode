'''
are all num seperated as element in array or as a string of number? -> array of number
integer only or negative? -> int only
is input are distinct number?
should the permutaion have duplicate? input [1,2,2,3] will have duplicate
-> unique permutation only

plan:
- to generate permutation, pick the char in the unused remaining number in the array

                            []
                        a/.            \b
                    [a]                  b]
      a used,         \ unused b.     a /.  \b used, invalid
                        [ab].         [ba]

    => [ab], [ba] n! = 2! = 4

- state to track: number used or not
- know this is solution: len == len(number) means all number are used
- arrage the remaining used number in the array

used as list of bool -> if used, change false to true 

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        def dfs(start): #start_index is used to keep track of the current level of the state-space tree we are in
            if start == len(nums):
                res.append(path[:])
            #check used number or not, if True (=used) we skip it, move to next number
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                path.append(num)
                used[i] = True #alr used and in current path
                dfs(start + 1)
                path.pop() #remove the number after find solution
                used[i] = False #backtrack, so remove the num, change to used
        dfs(0)
        return res


        