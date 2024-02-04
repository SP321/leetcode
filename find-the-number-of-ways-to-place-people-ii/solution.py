
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda a: (a[0], -a[1]))
        ans = 0
        for i in range(n):
            max_y = -inf
            for j in range(i + 1, n):
                if points[i][1] >= points[j][1] > max_y:
                    ans += 1
                    max_y = points[j][1]
        return ans