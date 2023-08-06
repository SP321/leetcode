class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        half = n // 2

        left = [sum(comb) for i in range(half + 1) for comb in combinations(nums[:half], i)]
        right = [sum(comb) for i in range(n - half + 1) for comb in combinations(nums[half:], i)]

        left.sort()

        ans = float('inf')
        for x in right:
            r = goal - x
            p = bisect.bisect_left(left, r)
            if p < len(left):
                ans = min(ans, abs(goal - (x + left[p])))
            if p > 0:
                ans = min(ans, abs(goal - (x + left[p - 1])))
        return ans