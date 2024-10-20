class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        c = Counter()
        i = 0
        for j in range(len(s)):
            c[s[j]] += 1
            while c[s[j]] == k:
                c[s[i]] -= 1
                i += 1
            ans += i
        return ans
