'''
- iterate theo từng vị trí trong words, xong gặp cái nào là return cái đó liền -> the first
- check dau cuoi cua 1 phan tu -> set the pointer in the loop so that the pointer can be reset each loop for the new word in the words 

'''
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        for word in words:
            if isPalindrome(word):
                return word
        return ""