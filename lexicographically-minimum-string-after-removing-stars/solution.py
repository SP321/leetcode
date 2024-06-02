class Solution:
    def clearStars(self, s: str) -> str:
        h=[]
        for i,x in enumerate(s):
            if x!='*':
                heappush(h,(x,-i))
            else:
                heappop(h)
        return ''.join([ch for (ch,_) in sorted(h,key=lambda x:-x[-1])])