class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []
        if not digits: return self.ans
        phone_map = {
		    '2': 'abc',
		    '3': 'def',
		    '4': 'ghi',
		    '5': 'jkl',
		    '6': 'mno',
		    '7': 'pqrs',
		    '8': 'tuv',
		    '9': 'wxyz'
        }
        def backtrack(current, next_digits):
            if len(next_digits) == 0: 
                self.ans.append(current[:])
                return 
		    
            for letter in phone_map[next_digits[0]]:
                backtrack(current + letter, next_digits[1:])
            
        backtrack("", digits)
            
        return self.ans
