class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(list(range(1,n+1)),k)