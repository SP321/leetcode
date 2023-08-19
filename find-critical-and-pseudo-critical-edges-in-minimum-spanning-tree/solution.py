class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = [1] * n # count instead of rank to check if mst is complete.
        self.max_size=0
        self.n=n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): #return boolean is_set_changed.
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.count[rootX] < self.count[rootY]:
                self.parent[rootX] = rootY
                self.count[rootY] += self.count[rootX]
                self.max_size=max(self.max_size,self.count[rootY])
            else:
                self.parent[rootY] = rootX
                self.count[rootX] += self.count[rootY]
                self.max_size=max(self.max_size,self.count[rootX])
            return True
        return False

    def is_everything_connected(self):
        return self.max_size==self.n
    

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexes_sorted = list(range(len(edges)))
        indexes_sorted.sort(key=lambda x: edges[x][2])

        def get_mst_weight(exclude_edge_index=-1, include_edge_index=-1):
            uf = UnionFind(n)
            ans = 0
            c = 0

            if include_edge_index != -1:
                u, v, w = edges[include_edge_index]
                if uf.union(u, v):
                    ans += w
                    c += 1

            for i in indexes_sorted:
                if i != exclude_edge_index:
                    u,v,w=edges[i]
                    if uf.union(u, v):
                        ans += w
                        c += 1

            return ans if c == n - 1 else float('inf')
        
        mst_weight = get_mst_weight()
        critical, pseudo_critical = [], []
        
        for i in indexes_sorted:
            mst_weight_without_current = get_mst_weight(exclude_edge_index=i)
            mst_weight_with_current = get_mst_weight(include_edge_index=i)
            
            if mst_weight_without_current > mst_weight:
                critical.append(i)
            elif mst_weight_without_current == mst_weight and mst_weight_with_current == mst_weight:
                pseudo_critical.append(i)
        
        return [critical, pseudo_critical]