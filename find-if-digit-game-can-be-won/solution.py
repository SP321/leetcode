class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a=sum(nums)
        b=sum(x for x in nums if x<10)
        if a==b*2:
            return False
        return True