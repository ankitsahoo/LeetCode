class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            c_bit = (c >> i) & 1
            if c_bit == 1:
                if a_bit == 0 and b_bit == 0:
                    flips += 1
            else:
                if a_bit == 1:
                    flips += 1
                if b_bit == 1:
                    flips += 1
        return flips
