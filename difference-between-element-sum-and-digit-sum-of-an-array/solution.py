class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a=sum(nums)
        b=sum(sum(map(int,str(x))) for x in nums)
        return a-b