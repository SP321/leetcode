class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n=len(satisfaction)
        satisfaction.sort()
        @cache
        def dfs(i,j):
            if i==n:
                return 0
            take=dfs(i+1,j+1) + satisfaction[i]*j
            leave=dfs(i+1,j)
            return max(take,leave)
        return dfs(0,1)