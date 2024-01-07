class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
            for i in range(1,9):
                x=i*dx+a
                y=i*dy+b
                if (x,y)==(c,d):
                    break
                if (x,y)==(e,f):
                    return 1

        for dx in [-1,1]:
            for dy in [-1,1]:
                for i in range(1,9):
                    x=i*dx+c
                    y=i*dy+d
                    if (x,y)==(a,b):
                        break
                    if (x,y)==(e,f):
                        return 1

        return 2