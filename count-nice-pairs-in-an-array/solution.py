class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        x=[i-int(str(i)[::-1]) for i in nums]
        c=Counter()
        ans=0
        for i in x:
            ans+=c[i]
            ans%=10**9+7
            c[i]+=1
        return ans