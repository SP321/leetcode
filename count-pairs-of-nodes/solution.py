class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cnt, ans = [0] * (n + 1), [0] * len(queries)
        shared = Counter((min(n1, n2), max(n1, n2)) for n1, n2 in edges)
        for n1, n2 in edges:
            cnt[n1] += 1
            cnt[n2] += 1
        sorted_cnt = sorted(cnt)
        for k, q in enumerate(queries):
            i, j = 1, n 
            while i < j:
                if q < sorted_cnt[i] + sorted_cnt[j]:
                    ans[k] += j - i
                    j -= 1
                else:
                    i += 1
            for (i, j), sh_cnt in shared.items():
                if q < cnt[i] + cnt[j] and q + sh_cnt >= cnt[i] + cnt[j]:
                    ans[k] -= 1
        return ans