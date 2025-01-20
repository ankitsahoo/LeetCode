class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write = 0
        read = 0
        
        while read < n:
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
