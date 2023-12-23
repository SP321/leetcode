class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        ans = [0] * n
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
    
        def dfs(node, parent):
            s = 1
            ma = []
            mi = []

            for neighbor in g[node]:
                if neighbor == parent:
                    continue
                size, ma_2, mi_2 = dfs(neighbor, node)
                s += size

                ma += ma_2
                mi += mi_2

            ma.append(cost[node])
            mi.append(cost[node])
            ma = sorted(ma)[-3:]
            mi = sorted(mi)[:2]

            if s >= 3:
                max_product = max(0, max(math.prod(ma), math.prod(mi) * max(ma)))
                ans[node] = max_product
            else:
                ans[node] = 1

            return s, ma, mi
        dfs(0, -1)
        return ans