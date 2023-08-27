class Solution:
    def canCross(self, stones: List[int]) -> bool:
        s1=set(stones)
        @cache
        def dfs(i,prev_k):
            print(i,prev_k)
            if i==stones[-1]:
                return True
            moves=[prev_k-1,prev_k,prev_k+1]
            ans=False
            for j in moves:
                if i+j in s1 and j>0:
                    ans=ans or dfs(i+j,j)
            return ans
        if stones[1]!=1:
            return False
        return dfs(1,1)