class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=0
        for bit in range(32):
            ans+=(x>>bit&1)^(y>>bit&1)
        return ans