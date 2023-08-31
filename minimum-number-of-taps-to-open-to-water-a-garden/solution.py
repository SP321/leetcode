
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        a = []
        for i, d in enumerate(ranges):
            a.append([i - d, i + d])
        a.sort(key=lambda x: [x[0], -x[1]])

        ans = 0
        i = 0
        watered = 0
        while watered < n:
            can_water_to = watered
            while i < len(a) and a[i][0] <= watered:
                can_water_to = max(can_water_to, a[i][1])
                i += 1
            if can_water_to == watered:
                return -1
            watered = can_water_to
            ans += 1
        
        return ans