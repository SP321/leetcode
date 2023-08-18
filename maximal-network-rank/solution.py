class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        direct = set()
        for a, b in roads:
            count[a] += 1
            count[b] += 1
            direct.add((a, b))
            direct.add((b, a))
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = count[i] + count[j]
                if (i, j) in direct:
                    rank -= 1
                ans = max(ans, rank)

        return ans