class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        c = Counter(map(tuple, coordinates))
        ans = 0
        if k == 0:
            for count in c.values():
                ans += (count * (count - 1)) // 2
            return ans

        for (a, b) in c.keys():
            for x_part in range(k+1):
                y_part = k - x_part
                x = a ^ x_part
                y = b ^ y_part
                if (x, y) in c and (x, y) != (a, b):
                    ans += c[(a, b)] * c[(x, y)]
        return ans//2
        