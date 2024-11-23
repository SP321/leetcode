class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        ans=0
        @cache
        def cost(x,y):
            xx=x
            r=0
            while x%26!=y:
                r+=nextCost[x%26]
                x+=1
            x=xx+26
            l=0
            while x%26!=y:
                l+=previousCost[x%26]
                x-=1
            return min(l,r)
        for x,y in zip(s,t):
            x=ord(x)%32-1
            y=ord(y)%32-1
            ans+=cost(x,y)
        return ans
            