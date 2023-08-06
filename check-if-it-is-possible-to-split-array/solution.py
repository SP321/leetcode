class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        @cache
        def dfs(i, j):
            if i == j:
                return True
            if prefix[j+1]-prefix[i]<m:
                return False
            for k in range(i, j):
                if dfs(i, k) and dfs(k+1, j):
                    return True
            return False
        if n==1:
            return True
        i=0
        j=n-1
        if i==j:
            return
        for k in range(i, j):
            if dfs(i, k) and dfs(k+1, j):
                return True
        return False