class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD=int(1e9+7)
        nums.sort()
        n=len(nums)
        ans=0
        dp={(i,inf):1 for i in range(n)}
        for _ in range(k-1):
            dp2=defaultdict(int)
            for key,value in dp.items():
                i,diff=key
                for j in range(i+1,n):
                    dp2[(j,min(diff,nums[j]-nums[i]))]+=value
            dp=dp2
        ans=0
        for key,times in dp.items():
            score=key[1]
            ans+=score*times
            ans%=MOD
        return ans