class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowSize = len(p)
        checkFreq = Counter(p) #O(n)
        print("checkFreq",checkFreq)
        windowFreq = Counter(s[0:windowSize]) # O(n)
        print('winFreq', windowFreq)
        res = []
        print("after")

        if checkFreq == windowFreq:
            res.append(0) #first anagram

        for right in range(windowSize, len(s)):
            left = right - windowSize
            windowFreq[s[left]] -= 1 #we remove previous left val in the new window
            if windowFreq[s[left]] == 0:
                del windowFreq[s[left]]
            windowFreq[s[right]] += 1
            print('winFreq', windowFreq)
            print("------")
            if checkFreq == windowFreq:
                res.append(left+1) #left + 1 is the new start idx of current window
                print("left+1", left + 1)
                print("------")
                #left is the old window
        return res
