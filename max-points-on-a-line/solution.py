from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            slope_counts = {}
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float('inf')
                    intercept = p1[0]
                else:
                    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
                    intercept = p1[1] - slope*p1[0]
                key = (slope, intercept)
                slope_counts[key] = slope_counts.get(key, 0) + 1
            if slope_counts:
                ans = max(ans, max(slope_counts.values())+1)
            else:
                ans = max(ans, 1)
        return ans