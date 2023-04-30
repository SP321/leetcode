class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return 0
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        elif self.rank[b] > self.rank[a]:
            a, b = b, a
        self.parent[b] = a
        self.n-=1
        return 1
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ua=UnionFind(n)
        ub=UnionFind(n)
        c=0
        for t,u,v in edges:
            if t==3:
                x=ua.union(u,v)
                y=ub.union(u,v)
                if x==1 or y==1:
                    c+=1
        for t,u,v in edges:
            if t==1:
                c+=ua.union(u,v)
            if t==2:
                c+=ub.union(u,v)
        if ua.n==1 and ub.n==1:
            return len(edges)-c
        return -1