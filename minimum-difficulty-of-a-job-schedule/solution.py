class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n=len(jobDifficulty)
        @cache
        def dfs(i,d,cur):
            if i==n and d==0:
                return cur
            if i==n or d==0:
                return float('inf')
            cur=max(cur,jobDifficulty[i])
            return min(
                dfs(i+1,d,cur),
                dfs(i+1,d-1,0)+cur,
            )
        ans=dfs(0,d,0)
        return ans if ans!=float("inf") else -1

