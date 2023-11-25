class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = list(accumulate(nums,initial=0))

        ans = [0] * n

        for i in range(n):
            left_sum = i * nums[i] - prefix_sum[i]
            right_sum = (prefix_sum[n] - prefix_sum[i + 1]) - (n - i - 1) * nums[i]
            ans[i] = left_sum + right_sum

        return ans