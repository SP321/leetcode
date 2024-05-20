class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for x in combinations(nums,i+1):
                ans+=reduce(xor,x)
        return ans