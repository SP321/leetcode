class Solution:
    def earliestSecondToMarkIndices(self, a: List[int], b: List[int]) -> int:
        n=len(a)
        m=len(b)
        f=set()
        firsts=set()
        total=sum(a)
        b=[x-1 for x in b]
        for i,x in enumerate(b):
            if x not in f and a[x]>1:
                f.add(x)
                firsts.add(i)
        
        def check(k):
            h=[]
            mark=0
            for i in range(k-1,-1,-1):
                if i in firsts:
                    heappush(h,a[b[i]])
                    if mark:
                        mark-=1
                    else:
                        mark+=1
                        heappop(h)
                else:
                    mark+=1
            return total-sum(h)+len(a)-len(h)<=mark
        pos=bisect.bisect_left(range(1,m+1),True,key=check)
        if pos==m:
            return -1
        return pos+1


