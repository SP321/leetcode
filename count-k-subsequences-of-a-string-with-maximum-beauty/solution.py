class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        md = 10 ** 9 + 7
        f = Counter(s)
        if len(f) < k:
            return 0
        freqs = list(f.values())
        top_k_sum = sum(heapq.nlargest(k, freqs))

        n = len(freqs)

        @cache
        def dp(i, k, target):
            if k == 0:
                return 1 if target == 0 else 0
            if i == n:
                return 0
            ans = dp(i + 1, k, target)
            ans += dp(i + 1, k - 1, target - freqs[i]) * freqs[i]
            return ans % md

        return dp(0, k, top_k_sum)