class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        graph = defaultdict(set)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0:
                    graph[i].add(j)
                    graph[j].add(i)

        dp = [[-1]*n for _ in range(1<<n)]

        def dfspath(mask, i):
            if dp[mask][i] != -1:
                return dp[mask][i]
            if mask == (1 << n) - 1:
                return 1
            count = 0
            for j in graph[i]:
                if not ((mask >> j) & 1):
                    count += dfspath(mask | (1 << j), j)
                    count %= MOD
            dp[mask][i] = count
            return count

        ans = 0
        for i in range(n):
            ans += dfspath(1<<i, i)
            ans %= MOD
        return ans