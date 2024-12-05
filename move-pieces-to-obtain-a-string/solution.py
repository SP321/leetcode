class Solution:
    def canChange(self, start: str, target: str) -> bool:
        p1,p2=0,0
        while p1<len(start) or p2<len(target):
            while p1<len(start) and start[p1]=='_':
                p1+=1
            while p2<len(target) and target[p2]=='_':
                p2+=1
            if p1<len(start) and p2<len(target):
                if start[p1]!=target[p2] or (start[p1]=='L' and p1<p2) or (start[p1]=='R' and p1>p2):
                    return False
            elif p1<len(start) or p2<len(target):
                return False
            p1+=1
            p2+=1
        return True