class Solution:
    def maximumScore(self, A: List[List[int]]) -> int:
        N = len(A)
        B = [list(accumulate(col, initial=0)) for col in zip(*A)]
        
        pdp = pep = ep = [0] * (N + 1)
        for j in range(1, N):
            dp = [0] * (N + 1)
            ep = [0] * (N + 1)
            for pb in range(N + 1):
                for cb in range(N + 1):
                    pv = B[j-1][cb] - B[j-1][pb] if cb > pb else 0
                    cv = B[j][pb] - B[j][cb] if cb < pb else 0
                    dp[cb] = max(dp[cb], pv + pdp[pb], pep[pb])
                    ep[cb] = max(ep[cb], cv + pep[pb], cv + pv + pdp[pb])
            
            pdp, pep = dp, ep
        
        return max(ep)