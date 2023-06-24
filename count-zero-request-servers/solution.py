class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        l, r = 0, 0
        m = len(queries)
        ans = [None] * m
        c = defaultdict(int)
        order=list(range(m))
        order.sort(key=lambda x: queries[x])
        for i in order:
            query=queries[i]
            while r < len(logs) and logs[r][1] <= query:
                c[logs[r][0]] += 1
                r += 1
            while l < len(logs) and logs[l][1] < query - x:
                c[logs[l][0]] -= 1
                if c[logs[l][0]] == 0:
                    del c[logs[l][0]]
                l += 1
            ans[i] =n-len(c)
        return ans
    