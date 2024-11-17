class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        def check(k):
            ops=[0]*(n+1)
            for i in range(k):
                l,r,val=queries[i]
                ops[l]-=val
                ops[r+1]+=val
            offset=0
            for i in range(n):
                offset+=ops[i]
                if nums[i]+offset>0:
                    return False
            return True

        ans=bisect_left(range(len(queries)+1),True,key=check)
        if ans<=len(queries):
            return ans
        return -1