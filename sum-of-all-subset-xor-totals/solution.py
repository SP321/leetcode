class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        def dfs(i,x):
            nonlocal ans
            if i==n:
                ans+=x
                return
            dfs(i+1,x^nums[i])
            dfs(i+1,x)
        dfs(0,0)
        return ans