class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        citations.sort()
        def check(k):
            pos=bisect_left(citations,k)
            if (n-pos)>=k:
                return 0
            return 1
        return bisect_left(range(len(citations)+1),1,key=check)-1