class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        a=set(nums)
        ans=1
        for x in sorted(a):
            c=1
            while x*x in a:
                a.discard(x)
                x=x*x
                c+=1
            ans=max(ans,c)
        return ans if ans>=2 else -1
            