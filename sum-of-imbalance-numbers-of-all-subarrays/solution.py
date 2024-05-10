class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            s, c  = set([x]), 0
            for y in nums[i+1:]:
                if y not in s:
                    s.add(y)
                    c+= 1 - ((y-1 in s) + (y+1 in s))
                ans+= c
        return ans