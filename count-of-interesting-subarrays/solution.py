class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        cnt = 0
        d = defaultdict(int)
        d[0] = 1
        for i in nums:
            if i % modulo == k:
                cnt += 1
            target = (cnt + modulo - k) % modulo
            ans += d[target]
            d[cnt % modulo] += 1
        return ans