class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n=len(bottomLeft)
        ans=0
        for i in range(n):
            x1,y1=bottomLeft[i]
            x2,y2=topRight[i]
            if x1<x2 and y1<y2:
                for j in range(i+1,n):
                    xx1,yy1=bottomLeft[j]
                    xx2,yy2=topRight[j]
                    if xx1<xx2 and yy1<yy2:
                        s=min(xx2,x2)-max(xx1,x1)
                        s2=min(yy2,y2)-max(yy1,y1)
                        if s>0 and s2>0:
                            ans=max(ans,min(s,s2))
        return ans**2