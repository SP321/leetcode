class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dp(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            return sum([dp(target-i) for i in nums])
        
        return dp(target)