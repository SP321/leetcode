class Solution:
    def earliestSecondToMarkIndices(self, A: List[int], B: List[int]) -> int:
        firsts = {}
        for i, b in enumerate(B):
            if A[b - 1] and b not in firsts:
                firsts[b] = i
        
        firsts_inv = {i: b for b, i in firsts.items()}

        def possible(bound):
            # Is B[:bound] enough to clear A?
            pq = []
            mark = 0

            for i in range(bound - 1, -1, -1):
                if i in firsts_inv:
                    heappush(pq, A[firsts_inv[i] - 1])
                    
                    if mark:
                        mark -= 1
                    else:
                        mark += 1
                        heappop(pq)
                else:
                    mark += 1

            return sum(A) - sum(pq) + len(A) - len(pq) <= mark
        
        M=len(B)
        pos= bisect.bisect_left(range(M+1),True,key=possible)
        if pos==M+1:
            return -1
        return pos