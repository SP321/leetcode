class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.a = [(1<<30)-1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, w):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        self.a[xr]&=w&self.a[yr]
        if xr != yr:
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        x=DSU(n)
        for u, v, w in edges:
            x.union(u,v,w)
        ans=[]
        for s,e in query:
            if s==e:
                ans.append(0)
                continue
            p1=x.find(s)
            p2=x.find(e)
            if p1!=p2:
                ans.append(-1)
            else:
                ans.append(x.a[p1])
        return ans