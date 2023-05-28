class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp={}
        def dfs(l,r):
            if(l,r) in dp:
                return dp[(l,r)]
            if r-l==1:
                return 0
            cost=float("inf")
            for c in cuts:
                if l<c<r:
                    cost=min(cost,(r-l)+dfs(l,c)+dfs(c,r))
            if cost==float("inf"):
                cost=0
            dp[(l,r)]=cost
            return cost
        return dfs(0,n)