class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        ans=-1
        n=len(points)
        points.sort()
        for i in range(n):
            for j in range(i+1,n):
                x,y=points[i]
                x2,y2=points[j]
                if x==x2 or y==y2:
                    continue
                if [x,y2] in points and [x2,y] in points:
                    for k,(mx,my) in enumerate(points):
                        if [mx,my] in [[x,y],[x2,y2],[x,y2],[x2,y]]:
                            continue
                        if (x<=mx<=x2 and min(y,y2)<=my<=max(y,y2)):
                            break
                    else:
                        ans=max(ans,abs(x-x2)*abs(y-y2))
        return ans