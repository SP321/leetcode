class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        i, j = 0, 0
        m = len(queries)
        ans = [None] * m
        c = Counter()
        for qi in sorted(list(range(m)),key=lambda x: queries[x]):
            cur=queries[qi]
            while j < len(logs) and logs[j][1] <= cur:
                c[logs[j][0]] += 1
                j += 1
            while i < len(logs) and logs[i][1] < cur - x:
                c[logs[i][0]] -= 1
                if c[logs[i][0]] == 0:
                    del c[logs[i][0]]
                i += 1
            ans[qi] =n-len(c)
        return ans
    