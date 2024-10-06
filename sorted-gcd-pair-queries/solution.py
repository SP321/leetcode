class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        mx = max(nums)
        freq=Counter(nums)
        dp = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c=freq[g]
            for m in range(2 * g, mx + 1, g):
                c+=freq[m]
                dp[g] -= dp[m]
            dp[g]+=c*(c-1)//2

        dp=list(accumulate(dp))

        ans=[]
        for x in queries:
            pos=bisect_left(dp,x+1)
            ans.append(pos)

        return ans