class Solution:
    def kItemsWithMaximumSum(self, a: int, b: int, _: int, k: int) -> int:
        return min(k, a) - max(0, k - b - a)