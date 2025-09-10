class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0
        
        positive = True
        if s[i] == '-':
            positive = False
            i += 1
        elif s[i] == '+':
            i += 1
        
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
            if positive and res > INT_MAX:
                return INT_MAX
            if not positive and -res < INT_MIN:
                return INT_MIN
        
        return res if positive else -res