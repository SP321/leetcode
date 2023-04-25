class Solution:
    def reverseBits(self, n: int) -> int:
        bits=bin(n)[2:]
        reverse=bits[::-1]
        reverse=reverse+ '0'*(32-len(reverse))
        return int(reverse,2)
        