from sortedcontainers import SortedList
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        d=defaultdict(list)
        points=list(zip(xCoord,yCoord))
        points.sort()
        n=len(points)
        up={}
        for x,y in points:
            d[x].append(y)
        
        for x,ys in d.items():
            for y1,y2 in pairwise(ys):
                up[x,y1]=x,y2
        
        yxmap={}
        sl=SortedList()
        ans=-1
        for x in sorted(d.keys()):
            ys=d[x]
            for y1,y2 in pairwise(ys):
                if y1 in sl:
                    prev_x=yxmap[y1]
                    if (prev_x,y1) in up and up[prev_x,y1][1] == y2 :
                        ans=max(ans,(y2-y1)*(x-prev_x))
            for y in ys:
                while sl:
                    pos=sl.bisect_left(y)
                    if pos==len(sl) or sl[pos]>y:
                        pos-=1
                    remy=sl[pos]
                    remx=yxmap[sl[pos]]
                    if pos>=0 and up[remx,remy][1]>=y:
                        sl.pop(pos)
                    else:
                        break
            for y in ys[:-1]:
                if y not in sl:
                    sl.add(y)
                yxmap[y]=x
        return ans