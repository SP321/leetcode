class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq = set()
        count = int(math.sqrt(c))
        for i in range(count + 1):
            a2  = i ** 2
            sq.add(a2)
            if c - a2 in sq:
                return True
        return False