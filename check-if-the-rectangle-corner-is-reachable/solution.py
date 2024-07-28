class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


def distance(A, B):
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)


def sign(x):
    return -1 if x < 0 else 1


def segmentCircle(l1, l2, cpt, r):
    x1 = l1[0] - cpt[0]
    y1 = l1[1] - cpt[1]
    x2 = l2[0] - cpt[0]
    y2 = l2[1] - cpt[1]
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx*dx + dy*dy)
    D = x1 * y2 - x2 * y1
    discriminant = r*r*dr*dr - D*D
    if discriminant < 0:
        return []
    if discriminant == 0:
        xa = (D * dy) / (dr * dr)
        ya = (-D * dx) / (dr * dr)
        ta = (xa-x1)*dx/dr + (ya-y1)*dy/dr
        return [(xa + cpt[0], ya + cpt[1])] if 0 < ta < dr else []

    xa = (D * dy + sign(dy) * dx * math.sqrt(discriminant)) / (dr * dr)
    ya = (-D * dx + abs(dy) * math.sqrt(discriminant)) / (dr * dr)
    ta = (xa-x1)*dx/dr + (ya-y1)*dy/dr
    xpt = [(xa + cpt[0], ya + cpt[1])] if 0 < ta < dr else []

    xb = (D * dy - sign(dy) * dx * math.sqrt(discriminant)) / (dr * dr)
    yb = (-D * dx - abs(dy) * math.sqrt(discriminant)) / (dr * dr)
    tb = (xb-x1)*dx/dr + (yb-y1)*dy/dr
    xpt += [(xb + cpt[0], yb + cpt[1])] if 0 < tb < dr else []
    return xpt


def circleCircle(O0, r0, O1, r1):
    x0, y0 = O0
    x1, y1 = O1
    d = distance((x0, y0), (x1, y1))
    if d > r0 + r1:
        return None
    if d < abs(r0-r1):
        return None
    if d == 0 and r0 == r1:
        return None
    a = (r0**2-r1**2+d**2)/(2*d)
    h = math.sqrt(r0**2-a**2)
    x2 = x0+a*(x1-x0)/d
    y2 = y0+a*(y1-y0)/d
    x3 = x2+h*(y1-y0)/d
    y3 = y2-h*(x1-x0)/d

    x4 = x2-h*(y1-y0)/d
    y4 = y2+h*(x1-x0)/d

    return (x3, y3, x4, y4)


class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:

        n = len(circles)
        dsu = DSU(n + 2)

        left_top = n
        right_bot = n + 1

        for i, (x, y, r) in enumerate(circles):
            if distance((0, 0), (x, y)) <= r:
                return False
            if dist((X, Y), (x, y)) <= r:
                return False

            if segmentCircle((0, 0), (0, Y),  (x, y), r) or segmentCircle((X, Y), (0, Y),  (x, y), r):
                dsu.union(i, left_top)

            if segmentCircle((0, 0), (X, 0), (x, y), r) or segmentCircle((X, Y), (X, 0),  (x, y), r):
                dsu.union(i, right_bot)

            for j in range(i + 1, n):
                x2, y2, r2 = circles[j]
                intersect_pts = circleCircle((x, y), r, (x2, y2), r2)
                if intersect_pts == None:
                    continue
                x3, y3, x4, y4 = intersect_pts
                if (0 <= x3 <= X and 0 <= y3 <= Y) or (0 <= x4 <= X and 0 <= y4 <= Y):
                    dsu.union(i, j)

        return dsu.find(left_top) != dsu.find(right_bot)