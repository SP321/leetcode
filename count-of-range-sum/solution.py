from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        sl = SortedList()
        sl.add(0)
        for i in accumulate(nums):
            left= sl.bisect_left(i-upper)
            right= sl.bisect_right(i-lower)
            ans += right - left
            sl.add(i)
        return ans