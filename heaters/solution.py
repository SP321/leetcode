class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heaters= [float("-inf")] + heaters + [float("inf")]
        houses.sort()
        i = 0
        ans = 0
        for house in houses:
            while heaters[i]< house:
                i += 1
            left = house - heaters[i-1]
            right = heaters[i] - house
            ans = max(ans, min(left, right))
        return ans