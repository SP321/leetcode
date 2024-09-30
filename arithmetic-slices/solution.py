class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        i=0
        ans=0
        nums=[y-x for y,x in pairwise(nums)]
        n=len(nums)
        for j in range(n):
            while nums[i]!=nums[j]:
                i+=1
            ans+= max(0,j-i)
        return ans
