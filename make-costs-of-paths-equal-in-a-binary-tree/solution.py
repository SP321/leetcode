class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def dfs(i):
            ans=0
            if i*2+1<n:
                ans=max(ans,dfs(i*2+1))
            if i*2+2<n:
                ans=max(ans,dfs(i*2+2))
            return ans+cost[i]
        x=dfs(0)
        def dfs2(i,cur=x):
            cur-=cost[i]
            if i*2+2<n:
                l,a=dfs2(i*2+1,cur)
                r,b= dfs2(i*2+2,cur)
                cur_node=min(l,r)
                return cur_node,max(l,r)-cur_node+a+b
            else:
                return cur,0
        return dfs2(0)[1]