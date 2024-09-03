class Solution:
    '''
    - track the number frequency in the substring, compare to the k -> if the frequency of the number is less or equal 
    then keep that number in the substring
    - if the current number is exceed the k number, break the substring, start new substring by reducing the left pointer
    - have 2 pointer left and right to keep track of the subtring 
    - have a dict to keep track of the frency  of the number, after start a new subtring, pop the number in the left pointer

    nums = [1,2,3,1,2,3,1,2], k = 1
              l
                  r
    '''
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start, end = 0, 0
        max_len = 0
        map = {} #key is the num, val is frequency

        for end in range(len(nums)):
            if nums[end] not in map:
                map[nums[end]] = 1
                max_len = max(max_len, end-start+1)
               
            
            elif nums[end] in map:
                map[nums[end]] += 1
                while map[nums[end]] > k:
                    map[nums[start]] -= 1
                    start += 1
                max_len = max(max_len, end - start + 1)
        return max_len



