class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=inf
        for x in nums:
            ans=min(ans,sum(map(int,str(x))))
        return ans