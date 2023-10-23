class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and  n&int("1010101010101010101010101010101",2) and n.bit_count()==1