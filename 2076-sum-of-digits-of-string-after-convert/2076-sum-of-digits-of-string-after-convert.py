class Solution:
    '''
    edge case:
    - empty string?
    - is that all english lowercase?
    - 
    '''

    def getLucky(self, s: str, k: int) -> int:
        number_str = ""
        for ch in s:
            number_str += str(ord(ch) - ord('a') + 1) 

        for _ in range(k):
            digit_sum = 0
            for digit in number_str:
                digit_sum += int(digit)
            if digit_sum < 10:
                return digit_sum
            number_str = str(digit_sum)
        return int(number_str)
        