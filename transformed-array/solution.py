class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        ans=[None]*n
        for i in range(n):
            j=i+nums[i]
            j%=n
            ans[i]=nums[j]
        return ans