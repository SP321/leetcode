class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for i,x in enumerate(nums):
            left=bisect_left(nums,lower-x,lo=i+1)
            right=bisect_left(nums,upper-x+1,lo=i+1)
            ans+=right-left
        return ans