class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=target
        flags=0
        for a,b,c in triplets:
            if x==a and b<=y and c<=z:
                flags|=1
            if y==b and a<=x and c<=z:
                flags|=2
            if z==c and b<=y and a<=x:
                flags|=4
            if a<=x and b<=y and c<=z:
                flags|=8
        return flags==15
