class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        return True

        
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        s1=DSU(n+1)
        s2=DSU(n+1)
        c=0
        for t,u,v in edges:
            if t==3:
                a=s1.union(u,v)
                b=s2.union(u,v)
                c+=a or b
        c1,c2=0,0
        for t,u,v in edges:
            if t==1:
                c1+=s1.union(u,v)
            if t==2:
                c2+=s2.union(u,v)
        if c+c1==n-1 and c+c2==n-1:
            return len(edges)-c-c1-c2
        return -1