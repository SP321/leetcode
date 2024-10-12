class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        return [-1 if x==2 else x^ ( (x^(x+1)) >>1 ) ^ ( (x^(x+1)) >>2 )  for x in nums]