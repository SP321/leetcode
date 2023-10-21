import queue
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dq = deque()
        ans = nums[0]

        for i in range(n):
            dp[i] = nums[i] + max(dp[dq[0]], 0) if dq else nums[i]
            ans = max(ans, dp[i])
            
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            while dq and i - dq[0] >= k:
                dq.popleft()
            dq.append(i)

        return ans