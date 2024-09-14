class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        def lis(arr):
            arr.sort(key=lambda tup: (tup[0], -tup[1]))
            res = []
            for x,y in arr:
                if not res or y > res[-1]:
                    res.append(y)
                else:
                    i = bisect_left(res, y)
                    res[i] = y
            
            return len(res)
        mx, my = coordinates[k]
        coordinates.sort()
        left = [(x,y) for x,y in coordinates if x < mx and y < my]
        right = [(x,y) for x,y in coordinates if x > mx and y > my]
        return 1 + lis(left) + lis(right)