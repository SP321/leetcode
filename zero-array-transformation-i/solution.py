class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        a=[0]*(n+1)
        for l,r in queries:
            a[l]-=1
            a[r+1]+=1
        offset=0
        for i in range(n):
            offset+=a[i]
            if nums[i]+offset>0:
                return False
        return True