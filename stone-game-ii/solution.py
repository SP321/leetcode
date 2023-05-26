class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp={}
        def dfs(alice,i,m):
            if((alice,i,m)) in dp:
                return dp[(alice,i,m)]
            if i==n:
                return 0
            ma=0
            mi=1e9
            stones=0
            for x in range(1,2*m+1):
                j=i+x-1
                if j>=n:
                    break
                stones+=piles[j]
                move=dfs(not alice,j+1,max(m,x))
                ma=max(ma,stones+move)
                mi=min(mi,move)
            dp[(alice,i,m)]=ma if alice else mi
            return dp[(alice,i,m)]
        return dfs(True,0,1)


            