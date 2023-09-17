class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            if bin(i).count('1')==k:
                ans+=nums[i]
        return ans