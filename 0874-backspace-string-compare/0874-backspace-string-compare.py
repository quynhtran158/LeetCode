class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_stack(string: str) -> list:
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif char == "#" and stack:
                    stack.pop()
            return stack
        return build_stack(s) == build_stack(t)