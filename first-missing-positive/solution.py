class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        c=[0]*(n+2)
        for i in nums:
            if i>0 and i<=n:
                c[i]=1
        for i in range(1,n+2):
            if c[i]==0:
                return i