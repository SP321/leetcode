class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]=1
        for i,j in zip(moveFrom,moveTo):
            if j!=i:
                d[j]+=d[i]
                del d[i]
        return sorted(d.keys())
