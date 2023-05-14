class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size
        self.union_count = [0] * size

    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
                self.union_count[root1] += 1
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]
                if self.rank[root1] == self.rank[root2]: 
                    self.rank[root2] += 1
                self.union_count[root2] += 1
        else:
            self.union_count[root1] += 1


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        x=UnionFind(n)
        for i in edges:
            x.union(i[0],i[1])
        ans=0
        for i in range(n):
            if x.find(i)==i:
                node_c=x.size[i]
                edge_c=x.union_count[i]
                if edge_c==(node_c*(node_c-1))//2:
                    ans+=1
        return ans