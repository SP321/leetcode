class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        next_nodes = [[] for _ in range(n)]
        prev_nodes = [[] for _ in range(n)]
        seen = [0] * n
        counts = [[0] * 26 for _ in range(n)]
        saved = [-1] * n

        for edge in edges:
            next_nodes[edge[0]].append(edge[1])
            prev_nodes[edge[1]].append(edge[0])

        def dfs(x):
            if seen[x]:
                return -1
            if saved[x] != -1:
                return saved[x]

            seen[x] = 1
            max_count = -1
            for y in next_nodes[x]:
                result = dfs(y)
                if result == -1:
                    seen[x] = 0
                    return -1
                
                for i in range(26):
                    counts[x][i] = max(counts[x][i], counts[y][i])

                max_count = max(max_count, result)

            counts[x][ord(colors[x]) - ord('a')] += 1
            max_count = max(max_count, counts[x][ord(colors[x]) - ord('a')])
            saved[x] = max_count
            seen[x] = 0
            return max_count
        
        ans = -1
        for i in range(n):
            result = dfs(i)
            if result == -1:
                return -1
            ans = max(ans, result)

        return ans
