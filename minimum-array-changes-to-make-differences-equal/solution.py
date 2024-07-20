class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        c = Counter()
        n = len(nums)
        limits = [0]*(k+1)
        for x, y in zip(nums[:n//2], nums[n//2:][::-1]):
            c[abs(x-y)] += 1
            limit = max(max(x, y), k-min(x, y))
            limits[limit] += 1

        ans = inf
        limits = [0]+list(accumulate(limits))
        for target in c:
            two = limits[target]
            one = n//2-two-c[target]
            ans = min(ans, one + two*2)
        return ans