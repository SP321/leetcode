def sumn(n): return n * (n + 1) // 2

class Solution:
    def numberOfSubstrings(self, S: str) -> int:
        N = len(S)
        MAGIC = int(N ** 0.5) + 1
        zeros = [-1] + [i for i, c in enumerate(S) if c=='0'] + [N]
        ans = 0
        prev = -1
        for cur in zeros:
            ans += sumn(cur - prev - 1)
            prev = cur

        for num_zeros in range(1, MAGIC):
            for i in range(1, len(zeros) - num_zeros):
                j = i + num_zeros - 1
                L = zeros[i] - zeros[i-1]
                R = zeros[j+1] - zeros[j]
                
                base = num_zeros**2 + num_zeros - (zeros[j] - zeros[i] + 1)

                if base < L + R:
                    ans += L * R
                    ans -= sumn(max(0, base))
                    ans += sumn(max(0, base - L))
                    ans += sumn(max(0, base - R))

        return ans