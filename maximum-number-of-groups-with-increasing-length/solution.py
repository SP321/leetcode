class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        def check(x):
            total = sum(usageLimits)
            n = len(usageLimits)
            if total < (x ** 2 + x) // 2:
                return False
            curr = sum(usageLimits[:-x])
            req = 0
            for i in range(1, x + 1):
                req += i
                curr += usageLimits[n - x + i - 1]
                if curr < req:
                    return False
            return True
        usageLimits.sort()
        left, right = 1, len(usageLimits)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = max(ans,mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans