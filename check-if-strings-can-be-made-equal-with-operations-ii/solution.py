class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n=len(s1)
        x=[s1[i] for i in range(n) if i%2==0]
        y=[s1[i] for i in range(n) if i%2==1]
        a=[s2[i] for i in range(n) if i%2==0]
        b=[s2[i] for i in range(n) if i%2==1]
        
        return Counter(x)==Counter(a) and Counter(y)==Counter(b)
        