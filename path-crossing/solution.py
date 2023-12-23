class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        v=set([(x,y)])
        dirs = {
            "N": (-1, 0),
            "E": (0, 1),
            "W": (0, -1),
            "S": (1, 0)
        }
        for i in path:
            dx,dy=dirs[i]
            x=dx+x
            y=dy+y
            if(x,y) in v:
                return True
            v.add((x,y))
        return False
