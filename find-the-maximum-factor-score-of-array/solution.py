class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ans=reduce(lambda x,y:gcd(x,y),nums)*reduce(lambda x,y:lcm(x,y),nums)
        if len(nums)>1:
            for i in range(len(nums)):
                a=nums[:i]+nums[i+1:]
                ans=max(ans,reduce(lambda x,y:gcd(x,y),a)*reduce(lambda x,y:lcm(x,y),a))
        return ans