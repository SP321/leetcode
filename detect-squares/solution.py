class DetectSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        for (x2, y2), count in self.points.items():
            if abs(x1 - x2) != abs(y1 - y2) or x1 == x2 or y1 == y2:
                continue
            ans += count * self.points[(x1, y2)] * self.points[(x2, y1)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)