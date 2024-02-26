from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        x = SortedList()
        i=0
        for j, val in enumerate(nums):

            if j-i > indexDiff:
                x.discard(nums[i])
                i+=1

            x.add(val)
            pos = x.bisect_left(val)
            if pos > 0 and val - x[pos - 1] <= valueDiff:
                return True
            if pos < len(x)-1 and x[pos+1] - val <= valueDiff:
                return True
        return False