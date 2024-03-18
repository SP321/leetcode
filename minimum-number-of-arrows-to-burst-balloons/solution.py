class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[-1])
        reach=-inf
        ans=0
        for a,b in points:
            if a>reach:
                ans+=1
                reach=b
        return ans