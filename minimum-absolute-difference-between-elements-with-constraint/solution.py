class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        min_diff = float('inf')
        leftValues = []

        for i, num in enumerate(nums):
            if i-x>=0:
                bisect.insort(leftValues, nums[i-x])
            idx = bisect.bisect_left(leftValues, num)
            if idx > 0:
                min_diff = min(min_diff, abs(num - leftValues[idx-1]))

            if idx < len(leftValues):
                min_diff = min(min_diff, abs(num - leftValues[idx]))
                
        return min_diff