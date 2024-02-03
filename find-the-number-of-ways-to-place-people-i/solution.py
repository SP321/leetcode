class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
         n=len(points)
         ans=0
         for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
               x2,y2=points[j]
               if (x1<=x2 and y1>=y2) or (x1>=x2 and y1<=y2):
                  for k in range(n):
                     if k!=i and k!=j:
                        x,y=points[k]
                        if x>=min(x1,x2) and x<=max(x1,x2) and y>=min(y1,y2) and y<=max(y1,y2):
                           break
                  else:
                     ans+=1
         return ans