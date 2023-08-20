class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): #return boolean is_set_changed.
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootX] += 1
            return True
        return False

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

            if mst_weight_without_current > mst_weight:
                critical.append(i)
            else:
                mst_weight_with_current = get_mst_weight(include_edge_index=i)
                if mst_weight_with_current == mst_weight:
                    pseudo_critical.append(i)
        
        return [critical, pseudo_critical]