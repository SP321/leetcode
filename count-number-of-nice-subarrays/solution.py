class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=defaultdict(int)
        dp[0]=1
        c=0
        ans=0
        for x in nums:
            if x%2:
                c+=1
            dp[c]+=1
            if c-k in dp:
                ans+=dp[c-k]
        return ans