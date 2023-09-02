class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        ans = 0
        x = 0
        c = Counter()

        for i in range(k):
            x += nums[i]
            c[nums[i]] += 1

        if len(c) >= m:
            ans = max(ans, x)

        for i in range(k, len(nums)):
            a = nums[i - k]
            x -= a
            c[a] -= 1
            if c[a] == 0:
                del c[a]

            b = nums[i]
            x += b
            c[b] += 1

            if len(c) >= m:
                ans = max(ans, x)

        return ans