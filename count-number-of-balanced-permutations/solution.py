MOD = 10**9+7
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        num=list(map(int,num))
        n=len(num)
        sm=sum(num)
        if sm%2!=0:
            return 0
        ct=Counter(num)
        
        @cache
        def dp(i,lc,rc,ls):
            if ls<0 or lc<0 or rc<0:
                return 0
            if i==10:
                return int(ls==0 and lc==0 and rc==0)
            ans=0
            for l in range(ct[i]+1):
                r=ct[i]-l
                cur=dp(i+1,lc-l,rc-r,ls-(i*l))
                cur*=comb(rc,r)
                cur*=comb(lc,l)
                ans+=cur
            return ans%MOD
        return dp(0,n//2,n-n//2,sm//2)

        