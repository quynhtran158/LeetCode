class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        respectively add the letter from s1 and s2
        reach the end of either the string, add the rest of the string to the result

        '''
        left, right = 0, 0
        res = []
        while left < len(word1) and right < len(word2):
            res.append(word1[left])
            res.append(word2[right])
            left += 1
            right += 1
        if len(word1) > len(word2):
            res.append(word1[left::])
        else:
            res.append(word2[right::])
        return "".join(res)