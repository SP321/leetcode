MOD=10**9+7

@cache
def dp(x,left):
    if left==0:
        return 0
    if x==25:
        return dp(0,left-1)+dp(1,left-1)+1
    return dp(x+1,left-1)

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c=Counter(s)
        ans=0
        for ch,v in c.items():
            ans+=dp(ord(ch)-ord('a'),t)*v
            ans%=MOD
        return ans+len(s)