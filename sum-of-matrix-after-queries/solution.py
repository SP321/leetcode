class Solution:
    def matrixSumQueries(self, N: int, queries: List[List[int]]) -> int:
        n = N
        m = N
        ans = 0
        sr = set()
        sc = set()
        
        for t, i, v in queries[::-1]:
            if n == 0 or m == 0:
                break
            if t == 0 and i not in sr:
                ans += v * m
                n -= 1
                sr.add(i)
            elif t == 1 and i not in sc:
                ans += v * n
                m -= 1
                sc.add(i)
        return ans