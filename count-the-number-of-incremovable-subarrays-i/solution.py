class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n=len(nums)
        def check(x):
            for a,b in pairwise(x):
                if a>=b:
                    return False
            return True
        ans=0
        for i in range(n):
            for j in range(i+1,n+1):
                if check(nums[:i]+nums[j:]):
                    ans+=1
        return ans