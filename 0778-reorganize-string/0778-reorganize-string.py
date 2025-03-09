'''
- all english alphabet?
- any special character?
- any number?

count the number of unique char and compare to the length of s to decide whether we can fullfill the requirement or not using dict 
odd len:

even len: 

all unique, repeated char possible and imposssible
all unique: 

Input: s = "aaab"
Output: ""

4 char but a: 3, b: 1 => impossible to have unique adjacent char
'''
from heapq import heappush, heappop
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        char_count = Counter(s)
        max_freq = max(char_count.values())
        n = len(s)
        
        # Step 2: Check if the rearrangement is possible
        if max_freq > (n + 1) // 2:
            return ""
        
        # Step 3: Use a max heap to store character frequencies
        max_heap = []
        for char, freq in char_count.items():
            heappush(max_heap, (-freq, char))  # Max heap using negative frequency
        
        # Step 4: Construct the result string
        res = []
        while len(max_heap) >= 2:
            # Extract the two most frequent characters
            freq1, char1 = heappop(max_heap)
            freq2, char2 = heappop(max_heap)
            
            # Append them to result
            res.append(char1)
            res.append(char2)
            
            # Reduce frequency and push back if still available
            if freq1 + 1 < 0:
                heappush(max_heap, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heappush(max_heap, (freq2 + 1, char2))
        
        # If one character remains, add it to the result
        if max_heap:
            res.append(max_heap[0][1])
        
        return "".join(res)

        