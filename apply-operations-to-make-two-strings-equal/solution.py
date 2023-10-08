class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n=len(s1)
        @cache
        def dp(i,cur_flipped=False,free=False):
            if i==n:
                if free or cur_flipped:
                    return float('inf')
                else:
                    return 0
            ans=float('inf')
            if (s1[i]!=s2[i] and not cur_flipped) or (s1[i]==s2[i] and cur_flipped):
                ans=min(ans,1+dp(i+1,True,free)) #op1
                if free:
                    ans=min(ans,dp(i+1,free=False)) #op2
                else:
                    ans=min(ans,x+dp(i+1,free=True)) #op2
            else:
                ans=dp(i+1,False,free)
            #print(i,cur_flipped,free,ans)
            return ans
        ans=dp(0)
        return ans if ans!=float('inf') else -1