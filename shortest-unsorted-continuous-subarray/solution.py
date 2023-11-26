class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        is_same = [i for i in range(len(nums)) if nums[i]!=sorted_nums[i]]
        if not is_same:
            return 0
        return is_same[-1]-is_same[0]+1