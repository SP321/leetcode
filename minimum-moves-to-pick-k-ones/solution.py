class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        a = [i for i, x in enumerate(nums) if x == 1]
        n = len(a)
        pre = [0] + list(accumulate(a))
        min_sz = max(0, k - maxChanges)
        max_sz = min(n, min_sz + 3, k)
        ans = inf
        for sz in range(min_sz, max_sz + 1):
            for i in range(n - sz + 1):
                j = i + sz
                half = sz // 2
                cur = (k - sz) * 2 + (pre[j] - pre[j - half]) - (pre[i + half] - pre[i])
                ans = min(ans, cur)
        return ans
