class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Set of vowels, including uppercase
        s_list = list(s)  # Convert string to list to modify it
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move l right to the next vowel
            while l < r and s_list[l] not in vowels:
                l += 1
            # Move r left to the next vowel
            while r > l and s_list[r] not in vowels:
                r -= 1
            
            # Swap the vowels
            if l < r:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1

        return ''.join(s_list)  # Convert list back to string and return
