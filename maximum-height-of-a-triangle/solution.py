class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        cur=1
        r=True
        rr=red
        bb=blue
        while True:
            if r:
                if red>=cur:
                    red-=cur
                    cur+=1
                else:
                    break
            else:
                if blue>=cur:
                    blue-=cur
                    cur+=1
                else:
                    break
            r=not r
        ans1=cur
        cur=1
        r=False
        red=rr
        blue=bb
        while True:
            if r:
                if red>=cur:
                    red-=cur
                    cur+=1
                else:
                    break
            else:
                if blue>=cur:
                    blue-=cur
                    cur+=1
                else:
                    break
            r=not r
        return max(ans1-1,cur-1)
                