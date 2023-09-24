class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        dq = deque([0])

        for j in range(1, n):
            dp[j] = nums[j] + dp[dq[0]]

            while dq and dp[j] >= dp[dq[-1]]:
                dq.pop()

            dq.append(j)

            i = j - k
            if dq[0] == i:
                dq.popleft()

        return dp[-1]