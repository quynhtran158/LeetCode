'''
? is query word only 1 word or a list of query words
? all english keyword, no non-alphanumerice character
? what is the priority between capitalization vs vowel.

Example:
wordlist: Kite, Kito
query: kito 

kito vs Kite: vowel, case-insensitive
kito vs Kito: capitalization
what to return?


- capitalization: case-insensitive, if word in wordlist match all char with order the word in query -> word in wordlist
return the 1st word that match query's word from wordlist 
- check the consonant and its order to see if word in query match with the char with char order in word in wordlist, case-insensitive -> word in wordlist
return the 1st word that match query's word from wordlist 
- match exactly order, vowel, consonant and case-sensitive -> word in wordlist

not match return ""

approach: use hashmap and hash set
- exact match: store word in wordlist in a set, iterate thru query to find the matching word
- capitalization: hashmap, with value is the original word, key is the lower case version. use hashmap to be able to track the 1st matching word. when we check, if the first (or current word in hash) match with query, we return immediately and skip the rest => return the 1st matching 
- vowel: hashmap too, 

'''
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordExact= set(wordlist)
        wordCap = {}
        wordVowel = {}
        ans = []

        for word in wordlist:
            if word.lower() not in wordCap:
                wordCap[word.lower()] = word

        def replaceVowel(word):
            vowel = "aeiou"
            temp = []
            for c in word.lower():
                if c in vowel:
                    temp.append("*")
                else:
                    temp.append(c)
            return "".join(temp)


        for w in wordlist:
            if replaceVowel(w) not in wordVowel:
                wordVowel[replaceVowel(w)] = w

        for query in queries:
            #exact
            if query in wordExact:
                ans.append(query)
            #capitalization
            elif query.lower() in wordCap:
                ans.append(wordCap[query.lower()])
            #vowel
            elif replaceVowel(query) in wordVowel:
                ans.append(wordVowel[replaceVowel(query)])
            #empty
            else:
                ans.append("")
        return ans
            

        