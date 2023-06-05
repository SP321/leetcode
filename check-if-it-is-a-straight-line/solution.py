class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates)
        x1,y1=coordinates[0]
        x2,y2=coordinates[1]
        if x2-x1 == 0 :
            m=float("inf")
        else:
            m=(y2-y1)/(x2-x1)
        for i in range(n-1):
            x1,y1=coordinates[i]
            x2,y2=coordinates[i+1]
            if x2-x1 == 0 :
                m2=float("inf")
            else:
                m2=(y2-y1)/(x2-x1)
            if m!=m2:
                return False
        return True
