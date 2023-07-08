class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        x = []
        for i,j in itertools.pairwise(weights):
            x.append(i+j)
        return sum(heapq.nlargest(k - 1, x)) - sum(heapq.nsmallest(k - 1, x))