class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed):
            total_time = 0
            for i in range(len(dist) - 1):
                total_time += (dist[i] + speed - 1) // speed
            total_time += dist[-1] / speed
            return total_time

        left = 1
        right = 10**7
        while left < right:
            mid = (left + right) // 2           
            if check(mid) > hour:
                left = mid + 1
            else:
                right = mid

        return left if check(left) <= hour else -1