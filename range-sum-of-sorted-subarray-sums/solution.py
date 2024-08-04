class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        x=[0]+list(accumulate(nums))
        n=len(x)
        ans=[]
        for i in range(n):
            for j in range(i+1,n):
                ans.append(x[j]-x[i])
        ans.sort()
        return sum(ans[left-1:right])%(10**9+7)