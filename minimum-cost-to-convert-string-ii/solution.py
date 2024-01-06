class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        path = defaultdict(dict)
        for x, y, z in zip(original, changed, cost):
            if y not in path[x]:
                path[x][y] = z
            else:
                path[x][y] = min(path[x][y], z)
        
        dist = {}
        for x in path:
            dist[x] = {}
            dist[x][x] = 0
            hpq = [(0, x)]
            while hpq:
                d, u = heappop(hpq)
                if dist[x][u] == d and u in path:
                    for v in path[u]:
                        if v not in dist[x] or dist[x][v] > dist[x][u] + path[u][v]:
                            dist[x][v] = dist[x][u] + path[u][v]
                            heappush(hpq, (dist[x][v], v))

        original_len = set(len(s) for s in original)
        
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if source[i - 1] == target[i - 1]:
                dp[i] = dp[i - 1]
            for length in original_len:
                if i >= length and (s := source[i - length : i]) in dist and (t := target[i - length : i]) in dist[s]:
                    dp[i] = min(dp[i], dp[i - len(s)] + dist[s][t])
        return dp[-1] if dp[-1] < float('inf') else -1