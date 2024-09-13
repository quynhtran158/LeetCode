class Solution:
    '''
    reverse thang int, tinh n%10
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

        