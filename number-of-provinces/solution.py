class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        s=[False]*n
        def dfs(i):
            s[i]=True
            for j in range(n): 
                if isConnected[i][j]==1 and not s[j]:
                    dfs(j)
        ans=0
        for i in range(n):
            if not s[i]:
                dfs(i)
                ans+=1
        return ans