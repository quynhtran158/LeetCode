'''
Builds a Trie from all words in wordDict for efficient prefix matching
Uses DFS to recursively try breaking the string at different positions
For each position i from 1 to the length of remaining string:
Checks if s[:i] forms a valid word using the Trie
If valid, recursively processes the remaining substring s[i:]
Combines the current word with all valid segmentations of the remaining string
Returns all valid combinations joined with spaces
The base case occurs when the string is empty, returning an empty list within a list [[]] to properly combine with previous words in the recursion chain.

PLAN:
- build the trie then dfs
- build trie store all wordDict
 + each node 26 chars, stored as isEnd array to flag end of valid word
 + insert() to add word char by char, create node 
 + search(): given str has complete word in trie

 - backtrack (dfs): explore all valid segment of s 
 
 - build result: each recursive call return a list of word list
 s[:1] cat, dfs([:i]) return [[dog, sand]] -> cat, sand, dog

 TC: In the worst case, we might have O(2^n) possible segmentations (where every position could be a valid break point)
For each segmentation, we perform Trie searches which take O(m) where m is the word length
Overall: O(2^n * m) in the worst case

SC: Trie storage: O(total characters in dictionary * 26)
Recursion stack: O(n) maximum depth
Result storage: O(2^n) for all possible segmentations



'''
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word):
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def search(self, word):
        node = self
        for char in word:
            index =  ord(char) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.isEnd

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(remainingStr):
            #base case empty str return empty combination
            if not remainingStr:
                return [[]]
            result = []

            for i in range(1, len(remainingStr)+ 1):
                prefix = remainingStr[:i]
                if trie.search(prefix):
                    suffixCombinations = backtrack(remainingStr[i:])
                    for combination in suffixCombinations:
                        result.append([prefix] + combination)
            return result
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        allCombinations = backtrack(s)
        return [' '.join(combination) for combination in allCombinations]
