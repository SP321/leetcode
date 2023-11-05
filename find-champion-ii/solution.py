class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        s=set(list(range(n)))
        for u,v in edges:
            s.discard(v)
        if len(s)==1:
            return list(s)[0]
        return -1
        