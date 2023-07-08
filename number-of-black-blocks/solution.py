class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        d = {}
        for x, y in coordinates:
            for dx in [0, 1]:
                for dy in [0, 1]:
                    if 0 <= x-dx < m-1 and 0 <= y-dy < n-1:
                        block = (x-dx, y-dy)
                        d[block] = d.get(block, 0) + 1
        result = [0]*5
        for count in d.values():
            result[count] += 1
        result[0] = (m-1)*(n-1) - sum(result)
        return result