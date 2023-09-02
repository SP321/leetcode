class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans=[]
        for (x,y,r) in queries:
            ans.append(sum([1 for (a,b) in points if ((x-a)**2+(y-b)**2)**0.5<=r]))
        return ans
            
