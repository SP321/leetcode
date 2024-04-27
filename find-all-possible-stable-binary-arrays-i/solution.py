class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD=int(1e9)+7
        @cache
        def dp(a,b,prev):
            if a==0 and b==0:
                return 1
            ans=0
            if prev==None or prev==1:
                for i in range(1,min(a,limit)+1):
                    ans+=dp(a-i,b,0)
            if prev==None or prev==0:
                for i in range(1,min(b,limit)+1):
                    ans+=dp(a,b-i,1)
            return ans%MOD
        return dp(zero,one,None)