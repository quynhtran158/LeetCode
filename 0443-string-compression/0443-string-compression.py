class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0 #initialize 2 pointers

        while read < len(chars): 
            start = read
            # Find the end of the sequence of identical characters
            while read < len(chars) and chars[read] == chars[start]: #start marks the beginning of a sequence of identical characters. The inner loop increments the read pointer until a different character is found. This determines the end of the current sequence.
                read += 1
            
            # Write the character
            chars[write] = chars[start]
            write += 1
            #khúc này update write để nhảy tới cái index tiếp theo (đằng sau char để mà store số lần char xuất hiện)
            #The character at the start of the sequence is written to the position pointed by write, and then write is incremented.
            # If more than one, write the count

            count = read - start
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write