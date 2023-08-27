class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        @cache
        def dp(i, x):
            if i == n:
                return abs(x)
            ans = 0
            if moves[i] == 'L':
                ans = dp(i+1, x-1)
            elif moves[i] == 'R':
                ans = dp(i+1, x+1)
            else:
                ans = max(dp(i+1, x-1), dp(i+1, x+1))
            return ans
        return dp(0, 0)
            
            