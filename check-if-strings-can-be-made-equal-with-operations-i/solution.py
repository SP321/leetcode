class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        x=s1[0]+s1[2]
        y=s1[1]+s1[3]
        a=s2[0]+s2[2]
        b=s2[1]+s2[3]
        return (x==a or x==a[::-1]) and (y==b or y==b[::-1])
        