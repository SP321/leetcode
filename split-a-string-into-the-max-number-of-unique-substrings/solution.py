class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        seen = set()
        n = len(s)
        def backtrack(i, c):
            nonlocal ans
            if i == n:
                ans = max(ans, c)
                return

            for j in range(i+1, n+1):
                cur=s[i:j]
                if cur not in seen:
                    seen.add(cur)
                    backtrack(j,c+1)
                    seen.discard(cur)

        backtrack(0, 0)
        return ans