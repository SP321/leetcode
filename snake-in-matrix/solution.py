class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x,y=0,0
        d={
            "UP":(-1,0),
            "RIGHT":(0,1),
            "DOWN":(1,0),
            "LEFT":(0,-1),

        }
        for c in commands:
            dx,dy=d[c]
            x+=dx
            y+=dy
        return n*x+y
