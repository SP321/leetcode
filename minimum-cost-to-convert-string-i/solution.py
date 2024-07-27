class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g=defaultdict(lambda :inf)
        for u,v,w in zip(original,changed,cost):
            g[u,v]=min(g[u,v],w)
        for k in ascii_lowercase:
            for i in ascii_lowercase:
                for j in ascii_lowercase:
                    g[i,j]=min(g[i,j],g[i,k]+g[k,j])
        ans=0
        for a,b in zip(source,target):
            if a!=b:
                if g[a,b]!=inf:
                    ans+=g[a,b]
                else:
                    return -1
        return ans