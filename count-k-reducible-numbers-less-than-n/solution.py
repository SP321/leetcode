MOD = 10**9 + 7
@cache
def dp1(x):
    if x==1:
        return 0
    return dp1(x.bit_count())+1
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        n=len(s)
        s=list(s)
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                s[i]='1'
            else:
                s[i]='0'
                break
        s=''.join(s)
        MX=[s,'1'*n]
        @cache
        def dp(i,  mx_, cnt=0):
            mx=MX[mx_]
            if i == n:
                return cnt>0 and dp1(cnt)<k
            cur_max=int(mx[i])
            ans = 0
            for dig in range(0, cur_max + 1):
                next_mx_ = mx_!=0 or dig != cur_max
                ans += dp(i + 1, next_mx_, cnt+dig)
            return ans%MOD
        ans=dp(0,0,0)
        dp.cache_clear()
        return ans