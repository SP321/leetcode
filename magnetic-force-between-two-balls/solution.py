class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(k):
            c=m
            ban=-1
            for x in position:
                if x>ban:
                    ban=x+k-1
                    c-=1
                    if c==0:break
            return 1 if c>0 else 0
        return bisect_left(range(position[-1]),1,key=check)-1
