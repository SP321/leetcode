class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        x=[(i+j-1)//j for i,j in zip(dist,speed)]
        x.sort()
        for i,x in enumerate(x):
            if i>=x:
                return i
        return len(dist)