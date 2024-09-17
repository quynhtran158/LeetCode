class Solution:
    '''
    can i assume the array wil have at least 2 elements?
    what do you want me to return when i cannot find pair that sum up to the target?
    how many valid answer are there?

    brute force:
    - 2 loop
        1st loop to iterate through the 1st array
        2nd loop to iterate throught the 2nd array

    for each element in the 1st array, find a matching number in 2nd array by iterating throught the 2nd array
 -> O(n^2)
    
    to improve my solution, i am thinkigng about usign hashmap
    hashmap: key is the curr numebr in the array, and the value is its index    
    complement = target - current number that we checking
    - check the complement of the current number 
    -> if we can find -> return the curr Num and the complement ind
    -> if we cannot find it -> simply add a new pair of value of the current number

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #key: current number, value is the index
        
        for i, val in enumerate(nums):
            complement = target - val
            if complement in map:
                return [i,map[complement]]
            map[val] = i
        return -1
        