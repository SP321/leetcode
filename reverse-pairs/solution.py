from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        sl = SortedList()
        for i, x in enumerate(nums):
            pos = sl.bisect_right(x*2)
            ans += i-pos
            sl.add(x)
        
        return ans