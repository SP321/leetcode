class Solution:
    def stringCount(self, n: int) -> int:
        MOD=10**9+7
        if n<4:
            return 0
        @cache
        def dfs(i,state=0):      
            if i==n:
                return 1 if state==0b1111 else 0
            ans=0
            ans+=dfs(i+1,state|0b1)
            ans+=dfs(i+1,state|0b10)
            if state&0b100:
                ans+=dfs(i+1,state|0b1000)
            else:
                ans+=dfs(i+1,state|0b100)
            ans+=dfs(i+1,state)*23
            return ans%MOD
        return dfs(0)