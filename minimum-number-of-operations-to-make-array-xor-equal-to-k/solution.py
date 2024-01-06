class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        y=0
        for x in nums:
            y^=x
        return (y^k).bit_count()