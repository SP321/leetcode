class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        eventsx=Counter()
        eventsy=Counter()
        for x1,y1,x2,y2 in rectangles:
            eventsx[x1]+=1
            eventsx[x2-1]-=1
            eventsy[y1]+=1
            eventsy[y2-1]-=1
        
        def helper(events):
            cur=0
            zc=0
            keys=sorted(events.keys())
            for x in keys:
                cur+=events[x]
                if cur==0:
                    zc+=1
                    if zc==3:
                        return True
            return False
        return helper(eventsx) or helper(eventsy)