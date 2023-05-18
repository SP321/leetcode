class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        p=list(range(n))
        for u,v in edges:
            p[v]=u
        return[i for i in range(n) if i==p[i]]