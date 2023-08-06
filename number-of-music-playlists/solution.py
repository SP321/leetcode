class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        md = 10**9 + 7
        @cache
        def dp(to_pick,to_use):
            used=n-to_use
            if to_pick==0:
                return to_use==0
            return (
                max(0,to_use)*dp(to_pick-1,to_use-1)+  
                max(0,used-k)*dp(to_pick-1,to_use)
            )
        return dp(goal,n)%md