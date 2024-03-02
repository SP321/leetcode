class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        g=defaultdict(list)
        n=len(edges)+1
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))
        
        @cache
        def dfs(i,p=-1,d=0):
            ans= 1 if d==0 else 0
            for j,w in g[i]:
                if j!=p:
                    ans+=dfs(j,i,(d+w)%signalSpeed)
            return ans
                
        ans=[]
        for node in range(n):
            s=0
            ways=0
            for x,w in g[node]:
                cur=dfs(x,node,w%signalSpeed)
                ways+=cur*s
                s+=cur
            ans.append(ways)
        return ans