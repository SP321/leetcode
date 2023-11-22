class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s=0
        ans=0
        prev=-1
        for i in nums:
            if i>prev:
                s+=i
            else:
                s=i
            ans=max(ans,s)
            prev=i
        return ans
            