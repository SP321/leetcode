class Solution:
    def countSubstrings(self, s, t):
        n, m = len(s), len(t)

        def test(i, j):
            ans = pre = cur = 0
            for k in range(min(n - i, m - j)):
                cur += 1
                if s[i + k] != t[j + k]:
                    pre, cur = cur, 0
                ans += pre
            return ans
        return sum(test(i, 0) for i in range(n)) + sum(test(0, j) for j in range(1, m))
