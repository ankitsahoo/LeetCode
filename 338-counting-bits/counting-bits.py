class Solution:
    def countBits(self, num: int):
        # Return a list of the number of 1's in the binary representation of numbers from 0 to num
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
