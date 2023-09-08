class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mi, ma = 1, 1
        for i in nums:
            ma,mi = max(i * ma, i * mi, i),min(i * ma, i * mi, i)
            ans = max(ans, ma)
        return ans