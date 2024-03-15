class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(a-b for a,b in pairwise(target+[0]) if a>b)