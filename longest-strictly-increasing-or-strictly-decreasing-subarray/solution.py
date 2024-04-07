class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        def check(a):
            return all(a[i]>a[i-1] for i in range(1,len(a))) or all(a[i]<a[i-1] for i in range(1,len(a)))
        for i in range(n):
            for j in range(i+1,n+1):
                if check(nums[i:j]):
                    ans=max(ans,j-i)
        return ans
            