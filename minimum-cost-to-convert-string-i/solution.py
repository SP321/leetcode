class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g=defaultdict(lambda :float('inf'))
        for u,v,w in zip(original,changed,cost):
            g[u,v]=min(g[u,v],w)
        for k in range(ord('a'),ord('z')+1):
            for i in range(ord('a'),ord('z')+1):
                for j in range(ord('a'),ord('z')+1):
                    ch_i=chr(i)
                    ch_j=chr(j)
                    ch_k=chr(k)
                    g[ch_i,ch_j]=min(g[ch_i,ch_j],g[ch_i,ch_k]+g[ch_k,ch_j])
        ans=0
        for a,b in zip(source,target):
            if a!=b:
                if g[a,b]!=float("inf"):
                    ans+=g[a,b]
                else:
                    return -1
        return ans