class Solution:
    def largestPalindrome(self, N: int, K: int) -> str:
        pow10 = [1] * N
        for i in range(1, N):
            pow10[i] = pow10[i-1] * 10 % K
        
        ans = [9] * N

        @cache
        def dp(i, r):
            if i == (N + 1) // 2:
                return r == 0
            
            for d in range(9, -1, -1):
                ans[i] = ans[N-1-i] = d
                coeff = sum(pow10[j] for j in {i, N-1-i})
                r2 = (r + coeff * d) % K
                if dp(i + 1, r2):
                    return True
            
            return False

        dp(0, 0)
        return "".join(map(str, ans))