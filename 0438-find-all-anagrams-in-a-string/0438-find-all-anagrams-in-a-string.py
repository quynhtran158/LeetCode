class Solution:
    '''
    using sort to check: time: O(nlogn), space: O(1)
    return the first index of the anagram
    - determind anagram: check each char in both string respectively to find the matching char
    if reach the end of both strings and cannot find all matching char of check -> not anagram
    - index of the orginal will be reset to beginnign of window
    - using sliding window with size of len(check) to find the first index quicker

    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size = len(p)
        check_sorted = sorted(p)  # Sort once for comparison
        res = []
        # Iterate through all possible substrings of length `window_size`
        for left in range(len(s) - window_size + 1):
            window = s[left:left + window_size]
            
            if sorted(window) == check_sorted:  # Compare sorted versions
                res.append(left) # Return the first index

        return res  # If no anagram is found
        