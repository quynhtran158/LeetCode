'''
- exact match: store word in word list to set, if match query -> 
- capitalization: hashmap, key:val -> all lowercase query : original query word -> traverse query 
- vowel: hashmap key: val, word in wordlist with vowe remove as *: query

setup the condition for word list, then travers query in queries to check to find ans

'''
class Solution:
    def spellchecker(self, wordList: List[str], queries: List[str]) -> List[str]:
        wordExact = set(wordList)
        wordCap = {}
        wordVowel = {}
        res = []

        for word in wordList:
            if word.lower() not in wordCap:
                wordCap[word.lower()] = word

        def replaceVowel(word):
            vowel = "aieou"
            temp = []
            for c in word.lower():
                if c in vowel:
                    temp.append("*")
                else:
                    temp.append(c)
            return "".join(temp)
        
        #add processed word t
        for word in wordList:
            if replaceVowel(word) not in wordVowel:
                wordVowel[replaceVowel(word)] = word
        
        for query in queries:
            #exact
            if query in wordExact:
                res.append(query)
            #capitalization
            elif query.lower() in wordCap:
                res.append(wordCap[query.lower()])
            #vowel
            elif replaceVowel(query) in wordVowel:
                res.append(wordVowel[replaceVowel(query)])
            else: #empty
                res.append("")
        return res



