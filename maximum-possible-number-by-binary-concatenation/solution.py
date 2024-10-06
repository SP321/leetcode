

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:(x << y.bit_length()) + y,sorted(nums, key=cmp_to_key(lambda x,y: -1 if (x << y.bit_length()) + y > (y << x.bit_length()) + x else 1)))