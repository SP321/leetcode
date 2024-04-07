class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}
        
        def find(i):
            if i != uf[i]:
                uf[i] = find(uf[i])
            return uf[i]
        
        res = []
        for i, j in requests:
            success = True
            pi, pj = find(i), find(j)
            if pi != pj:
                for k, l in restrictions:
                    pk, pl = find(k), find(l)
                    if (pi, pj) == (pk, pl) or (pi, pj) == (pl, pk):
                        success = False
                        break
            if success:
                if rank[pi] < rank[pj]:
                    uf[pi] = pj
                else:
                    uf[pj] = pi
                    if rank[pi] == rank[pj]:
                        rank[pi] += 1
            res.append(success)
        return res