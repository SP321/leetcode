class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        ans = cur = 0
        for i, c in enumerate(s):
            cur ^= 1 << ('aeiou'.find(c) + 1) >> 1
            seen.setdefault(cur, i)
            ans = max(ans, i - seen[cur])
        return ans