class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans=0
        for i in range(min(n,limit)+1):
            remaining=n-i
            a = max(remaining - limit, 0)
            b = min(remaining, limit)
            if a <= b:
                ans += b - a + 1
        return ans
