'''
understand:
merge the string w1 and w2 interleaving, the rest of the longer string will be inserted right after the shorter string
- can i assume we all have lowercase english char?
- can i assume we will never have empty string in both w1 and w2?
- what is the maximum lenght of both string?
- do you want me to merge in-place?
plan:
- find the shorter len of the string
- merge the string interleavingly, the append the exceed string of longer string at the end
- have a new empty array to store the merged string

'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #new empty array to store merged string
        res = []
        min_len = min(len(word1), len(word2))
        
        #work for case which len w1= w2
        for i in range(min_len):
            res += word1[i]
            res += word2[i]
        
        if len(word1) > min_len:
            res += word1[min_len:] #if len w1 longer, add the rest of the char start from min_len index til the end of the word1

        if len(word2) > min_len:
            res += word2[min_len:]
        
        return "".join(res)
