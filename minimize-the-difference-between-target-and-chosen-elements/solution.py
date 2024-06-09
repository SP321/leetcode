class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        dp0=1
        for row in mat:
            dp1=0
            for x in row:
                dp1|=dp0<<x
            dp0=dp1
        ans=inf
        for bit in range(dp0.bit_length()):
            if dp0&(1<<bit):
                ans=min(ans,abs(target-bit))
        return ans