'''
clarify:
empty str? no
no palindrome partion, what to return? ""
all english alphabet? yes
non-numeric, symbol? no
all lowercase? yes (Doesnt matter)

We want to split the string into substrings where each substring is a palindrome. To do this, we use recursion (backtracking). 
At each position start, we try to take a prefix s[start:end]. 
We begin with the shortest prefix (length 1) and gradually increase the length (end moves from start+1 up to n). 
For each prefix, if it’s a palindrome, we slice it off and then recursively analyze the rest of the string starting at end. 
This way, we explore all possible partitions: first with short palindromes, then with longer ones. 
When start == n, it means we’ve reached the end, so the current path is a valid partition and we add it to the result.

start: the index where we begin cutting the string (the part that hasn’t been partitioned yet).
end: moves forward from start+1 to n, so s[start:end] creates substrings of increasing length.
By fixing start and moving end, we can generate all possible prefixes that begin at start.

We want to try every possible prefix starting at start:

The shortest prefix is 1 character → s[start:start+1].

The longest prefix is everything from start to the end → s[start:n].

To make sure we include s[start:n], our loop must let end reach n.

But because Python slices stop before end, the loop goes to n+1.

start là vị trí bắt đầu chuỗi aka chỗ bị cắt để tìm the remaing substring for recursion
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(word):
            return word == word[::-1]
        def dfs(start, path):
            if start == len(s):
                res.append(path[:]) #copy the path, at that state to track the current prefix
                #lưu nguyên list cur_path, cần copy ([:]). return list of list 
                return
            for end in range(start + 1, len(s)+1):
                prefix = s[start:end] #generates every possible substring starting at start.
                if isPalindrome(prefix):
                    dfs(end, path + [prefix]) #end ensures we move the starting point to after the prefix we just cut.
                    #creates a new path list that includes the current palindrome choice.
        dfs(0, [])
        return res
        