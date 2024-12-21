MOD=10**9+7
class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        l=Counter()
        r=Counter(nums)
        lr=Counter(nums)
        n=len(nums)
        def cnt(n,r):
            if n<r:
                return 0
            return comb(n,r)
        ans=0
        for i,x in enumerate(nums):
            lr[x]-=1
            r[x]-=1
            xl,nxl,xr,nxr=l[x],i-l[x],r[x],(n-i-1)-r[x]
            #2,2
            ans+=cnt(xl,2)            *       cnt(xr,2)

            #2,1
            #1,2
            ans+=cnt(xl,1)*cnt(nxl,1) *       cnt(xr,2)
            ans+=cnt(xl,2)            *       cnt(xr,1)*cnt(nxr,1)
            
            #1,1
            #0,2
            #0,2
            ans+=cnt(xl,1)*cnt(nxl,1) *       cnt(xr,1)*cnt(nxr,1)
            ans+=cnt(xl,2)            *       cnt(nxr,2)
            ans+=cnt(nxl,2)           *       cnt(xr,2)

            # 1,0 # all unique. total - choose atleast 2 same
            s2 = sum(cnt(r[y],2) for y in r)
            for y in l:
                if y!=x:
                    ss = s2-cnt(r[x],2)-cnt(r[y],2)
                    ans += l[x]*l[y]  *  (cnt(nxr-r[y],2)-ss)
            # 0,1  # all unique. total - choose atleast 2 same
            s1 = sum(cnt(l[y],2) for y in l)
            for y in r:
                if y!=x:
                    ss = s1-cnt(l[x],2)-cnt(l[y],2)
                    ans += (cnt(nxl-l[y],2)-ss)  *  r[x]*r[y]
                
            ans%=MOD
            lr[x]+=1
            l[x]+=1

        return ans