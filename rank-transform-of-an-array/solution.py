class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(set(arr))
        b={x:i+1 for i,x in enumerate(a)}
        return [b[x] for x in arr]