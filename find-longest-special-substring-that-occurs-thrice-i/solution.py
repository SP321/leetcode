class Solution:
    def maximumLength(self, s: str) -> int:
        prev=None
        c=1
        d=defaultdict(list)
        for i,x in enumerate(s):
            if x==prev:
                c+=1
            elif prev!=None:
                d[prev].append(c)
                c=1
            prev=x
        d[prev].append(c)
        ans=-1
        for x in d.values():
            ma=max(x)
            c1,c2=x.count(ma),x.count(ma-1)
            if c1>=3:
                ans=max(ans,ma)
            if c1>=2 and ma>=2:
                ans=max(ans,ma-1)
            if c2>=1 and ma>=2:
                ans=max(ans,ma-1)
            if ma>=3:
                ans=max(ans,ma-2)
        return ans