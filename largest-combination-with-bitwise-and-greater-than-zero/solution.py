class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max( sum(x>>bit&1 for x in candidates) for bit in range(24) )