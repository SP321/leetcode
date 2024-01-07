class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n=len(s)
        @cache
        def dp(i,move=True,current_bitmask=0):
            if i==n:
                return 1
            def calc_next(ch):
                next_bitmask=current_bitmask| (1<<(ord(ch)-ord('a')))
                c=0
                if next_bitmask.bit_count()>k:
                    c=1
                    next_bitmask=1<<(ord(ch)-ord('a'))
                return next_bitmask,c
            next_bitmask,c=calc_next(s[i])
            ans=dp(i+1,move,next_bitmask)+c
            if move:
                for c in range(ord('a'),ord('a')+26):
                    next_bitmask,c=calc_next(chr(c))
                    ans=max(ans,dp(i+1,False,next_bitmask)+c)
            return ans
        return dp(0)