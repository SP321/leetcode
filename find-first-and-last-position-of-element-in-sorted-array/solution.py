class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target)
        return [-1, -1] if start == end else [start, end - 1]