class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0 
        ans = 0
        # if len(s) == 0:
        #     return ans
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1 #shrink window by removing s[left] until window valid
            window.add(s[right])
            ans = max(ans, right-left+1)
        return ans
        