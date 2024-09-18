class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7":"pqrs",
            "8": "tuv",
            "9": "wxyz" 
        }
        
        ans = []
        def dfs(start_index: int, path: list) -> None:
            #base case la add het cac char cua cai so do
            if start_index == len(digits):
                ans.append("".join(path))
                return 
            next_number = digits[start_index]
            for char in keyboard[next_number]:
                path.append(char)
                dfs(start_index + 1, path)
                path.pop()
            return ans

        return dfs(0, [])


   