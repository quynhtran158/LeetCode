class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        #the shorter len str was fully added, the longer has remaining char
        res.append(word1[i::]) #add the rest of w1 from index i
        res.append(word2[j::]) #add the rest of w2 from index j
        return "".join(res)
