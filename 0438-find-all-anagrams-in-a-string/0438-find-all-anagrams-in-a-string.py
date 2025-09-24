class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowSize = len(p)
        checkFreq = Counter(p) #O(n)
        print("checkFreq",checkFreq)
        windowFreq = Counter(s[0:windowSize]) # O(n)
        res = []

        if checkFreq == windowFreq:
            res.append(0) #first anagram start index

        for right in range(windowSize, len(s)):
            left = right - windowSize #old left, old start of window
            windowFreq[s[left]] -= 1 #we remove previous left val in the new window, this is the old start, here we r sliding to new window so need remove old start (left), 
            # if windowFreq[s[left]] == 0: #clean the counter check, counter ignore 0 
            #     del windowFreq[s[left]]
            windowFreq[s[right]] += 1
            if checkFreq == windowFreq:
                res.append(left+1) #left + 1 is the new start idx of current window
                #left is the old window
        return res
