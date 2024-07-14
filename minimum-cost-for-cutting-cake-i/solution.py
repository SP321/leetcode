class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        h=[]
        for i,x in enumerate(horizontalCut):
                heappush(h,(-x,i,1))
        for j,x in enumerate(verticalCut):
                heappush(h,(-x,j,-1))
        c1=1
        c2=1
        ans=0
        while h:
            x,i,dir=heappop(h)
            x=-x
            if dir==1:
                c1+=1
                ans+=x*c2
            else:
                c2+=1
                ans+=x*c1
        return ans