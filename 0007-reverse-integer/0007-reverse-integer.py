class Solution:
    '''
    how to check the range
    2 pointer to reverse the integer first, then check the range -> either return 0 or the reverse valiue

    1, reverse use built- in function
    2. split the integer into array then use 2 pointer

    be careful of the sign
    '''

    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        x_str = str(abs(x)) #convert the int to string
        reversed_str = ""
        for i in range(len(x_str) -1, -1, -1): #reverse the string
            reversed_str += x_str[i]
            reversed_int = int(reversed_str) * sign

        if -2**31 <= reversed_int and reversed_int <= 2**31-1:
            return reversed_int
        else:
            return 0

        