from sortedcontainers import SortedList
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        d=defaultdict(list)
        points=list(zip(xCoord,yCoord))
        points.sort()
        n=len(points)
        for i in range(n):
            d[points[i][1]].append(i)
        st=set(points)
        qs=[]
        for y in d:
            for i,j in pairwise(d[y]):
                if j-i>=2:
                    if points[i+1][0]==points[i][0]:
                        j=bisect_left(points,(points[j][0],inf))-1
                        qs.append((i,j))
        
        block_size = int(n ** 0.5)
    
        def mo_cmp(x):
            block = x[0] // block_size
            return (block, x[1])
    
        qs.sort(key=mo_cmp)

    
        curr_l = 0
        curr_r = -1

        sl=SortedList()
        def add(idx):
            sl.add(points[idx][1])
    
        def remove(idx):
            sl.remove(points[idx][1])
    
        ans=-1
        for l, r in qs:
            while curr_r < r:
                curr_r += 1
                add(curr_r)
            while curr_r > r:
                remove(curr_r)
                curr_r -= 1
            while curr_l < l:
                remove(curr_l)
                curr_l += 1
            while curr_l > l:
                curr_l -= 1
                add(curr_l)
            x1,y1=points[l]
            x2,y2=points[r]
            if len(sl)>2:
                p1=sl.bisect_left(y1)
                p2=sl.bisect_left(y1+1)
                if p2-p1==2:
                    y3=sl[p2]
                    if (x2,y3) in st and (x1,y3) in st:
                        ans=max(ans,abs(x1-x2)*abs(y1-y3))
            
        return ans