class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        reach=-1
        ans=0
        for x,y in points:
            if x>reach:
                reach=x+w
                ans+=1
        return ans