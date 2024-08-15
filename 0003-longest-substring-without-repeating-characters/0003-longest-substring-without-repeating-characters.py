'''
plan: 

have a window, keep slding the window to find the longest none repeating char
put the visted char in a set, if we find a deupplicate, we cut of the window, until the window doesnt contain the char of right side
when we find a duplicate, we store the len of that window, then calc the max len later

we want to have left stay at the beginning then adjust left manually, and keep iterating through the array by right pointer so we will use while loop
s = "abcabcbb"
      l
         r

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        window = set()
        curr_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
                curr_len -= 1
            window.add(s[right])
            curr_len += 1
            max_len = max(curr_len, max_len)

            
        return max_len
                
