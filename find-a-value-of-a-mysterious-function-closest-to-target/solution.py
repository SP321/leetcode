class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        s, ans = set(), float('inf')
        for a in arr:
            s = {a & b for b in s} | {a}
            for c in s:
                ans = min(ans, abs(c - target))
        return ans