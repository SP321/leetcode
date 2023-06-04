class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        pos1=nums.index(1)
        pos2=nums.index(n)
        ans=0
        if pos2<pos1:
            ans-=1
        ans+=pos1
        ans+=n-pos2-1
        return ans