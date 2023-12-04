class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        @cache
        def dfs(i,left,cur_max):
            if left==0:
                return float("-inf")
            if i==n:
                return 0
            cur_max=max(cur_max,arr[i])
            ans=dfs(i+1,left-1,cur_max)
            ans=max(ans,dfs(i+1,k,0)+cur_max*(k-left+1))
            return ans
        return dfs(0,k,0)
            