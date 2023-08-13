class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i):
            if i == len(nums):
                return True
            ans = False
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                ans |= dfs(i + 2)
            if i + 2 < len(nums) and nums[i] == nums[i + 1] == nums[i + 2]:
                ans |= dfs(i + 3)
            if (i + 2 < len(nums) and 
                nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i] == 1):
                ans |= dfs(i + 3)
            return ans
        return dfs(0)