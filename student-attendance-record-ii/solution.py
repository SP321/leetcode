class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp0 = [[0 for _ in range(2)] for _ in range(3)]
        dp0[0][0] = 1
        for i in range(1, n + 1):
            dp1 = [[0 for _ in range(2)] for _ in range(3)]
            for a in range(3):
                for b in range(2):
                    dp1[0][b] = (dp1[0][b] + dp0[a][b]) % MOD
                    if b == 0:
                        dp1[0][1] = (dp1[0][1] + dp0[a][b]) % MOD
                    if a < 2:
                        dp1[a+1][b] = (dp1[a+1][b] + dp0[a][b]) % MOD
            dp0 = dp1

        ans = 0
        for a in range(3):
            for b in range(2):
                ans = (ans + dp0[a][b]) % MOD
        return ans