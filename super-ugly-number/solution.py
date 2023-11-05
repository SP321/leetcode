class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        size = len(primes)
        ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
        for i in range(1, n):
            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]
