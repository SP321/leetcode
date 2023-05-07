class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            pre=nums[:i+1]
            suffix=nums[i+1:]
            ans.append(len(set(pre))-len(set(suffix)))
        return ans
            