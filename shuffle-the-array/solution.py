class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for i in range(n) for x in [nums[i], nums[n+i]]]