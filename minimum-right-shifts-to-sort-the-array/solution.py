class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)):
            y=nums[i:]+nums[:i]
            if sorted(y)==y:
                ans=len(nums)-i if i!=0 else 0
        return ans