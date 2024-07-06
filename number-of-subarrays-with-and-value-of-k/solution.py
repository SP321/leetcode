class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp0=Counter()
        ans=0
        for x in nums:
            dp1=Counter([x])
            for y in dp0:
                dp1[y&x]+=dp0[y]
            dp0=dp1
            ans+=dp0[k]
        return ans