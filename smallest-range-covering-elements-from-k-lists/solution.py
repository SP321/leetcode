class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        d=Counter()
        for i,arr in enumerate(nums):
            for x in arr:
                d[x]|=1<<i
        a=sorted(d.keys())
        m=len(a)
        i=0
        start,end=0,a[-1]
        c=Counter()
        for j,x in enumerate(a):
            for bit in range(n):
                if (d[x]>>bit) &1 >0 :
                    c[bit]+=1
            while i<=j and len(c)==n:
                for bit in range(n):
                    if (d[a[i]]>>bit)&1 >0 :
                        c[bit]-=1
                        if c[bit]==0:
                            del c[bit]
                if a[j]-a[i]<end-start:
                    start,end=a[i],a[j]
                i+=1
        return start,end


