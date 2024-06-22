MOD=10**9+7
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        min_inv=[0]*n
        max_inv=[inf]*n
        for x,y in requirements:
            min_inv[x]=y
            max_inv[x]=y
        for i in range(1,n):
            min_inv[i]=max(min_inv[i-1],min_inv[i])
        for i in range(n-2,-1,-1):
            max_inv[i]=min(max_inv[i+1],max_inv[i])
        @cache
        def dp(i,c):
            if i==n:
                return 1
            ans=0
            for j in range(min_inv[i],max_inv[i]+1):
                if c<=j<=c+i:
                    ans+=dp(i+1,j)
            return ans%MOD
        return dp(0,0)