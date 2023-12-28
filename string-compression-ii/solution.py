class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n=len(s)
        @cache
        def dp(i,k,prev=None,c=0):
            if k<0:
                return float('inf')
            if i==n:
                return 0
            if s[i]==prev:
                if c in [1,9,99]:
                    return dp(i+1,k,prev, c+1)+1
                else:
                    return dp(i+1,k,prev, c+1)
            else:
                return min(dp(i+1,k-1,prev, c), dp(i+1,k,s[i],1)+1)
        return dp(0,k)