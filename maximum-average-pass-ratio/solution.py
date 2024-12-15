class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h=[]
        for x,y in classes:
            heappush(h,(x/y-(x+1)/(y+1),x,y))

        for _ in range(extraStudents):
            cur_ratio,x,y=heappop(h)
            x+=1
            y+=1
            heappush(h,(x/y-(x+1)/(y+1),x,y))

        n=len(classes)
        sm=0
        for _,x,y in h:
            sm+=x/y
        return sm/n