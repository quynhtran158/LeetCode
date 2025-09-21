'''
Intuition (how I’d explain to interviewer)
Each digit can map to multiple letters.
For an input string of length n, each position (digit) is like a "level" in a decision tree.
At each level, I choose one letter → go deeper → eventually build a string of length n.
This naturally forms a DFS/backtracking problem:
Try a letter
Recurse on the next digit
Backtrack (undo) to explore other letters.
So the solution space looks like a state-space tree where each path = one valid letter combination.

 Plan (step-by-step)
Edge cases:
-If input is empty → return [].
-Digits 0 and 1 don’t map to letters → return [] (or handle as invalid input).
-Repeated digits are fine → e.g., "22" produces "aa","ab","ac","ba","bb"....

- Mapping: Use a dictionary to map digits "2"–"9" to their letters.
- DFS/backtracking: Keep track of two things:
+ startIndex: which digit we’re currently processing.
+ path: the current partial combination (list of chosen letters).
-Base case: when startIndex == len(digits) → we’ve built a complete string → add to result.
-Recursive case: look at digits[startIndex], loop through its mapped letters:
- Append letter to path.
- Recurse with startIndex + 1.
- pop the letter (backtrack) to explore the next option.
- Return results at the end.


'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        KEYBOARD = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
        res = []
        if len(digits) == 0:
            return []

        def dfs(startIndex, path):
            if startIndex == len(digits): #reach the solution, have the letter 
                res.append(''.join(path)) #add the letter in path
                return 
            #go thru each number in digits input
            #go thru each letter of that current number until all letter are consider,
            #move to next number and its letter
            
            next_number = digits[startIndex] #keep track of the current number in digit input
            for letter in KEYBOARD[next_number]: #keep track of the letter of that number
                path.append(letter)
                dfs(startIndex + 1, path)
                path.pop()
        dfs(0, []) #first alr start with idx 0 and path is empty,
        return res