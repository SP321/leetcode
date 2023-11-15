class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def helper(i, j, n) :
            if n == 1:
                return s1[i] == s2[j]
            ans=False
            for k in range(1, n):
                ans = ans or \
                (helper(i, j, k) and helper(i + k, j + k, n - k)) or \
                (helper(i, j + n - k, k) and helper(i + k, j, n - k))
            return ans
        return helper(0, 0, len(s1))