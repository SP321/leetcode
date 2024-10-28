class Solution:
    def countLargestGroup(self, n: int) -> int:
        c=[0]*(37)
        for x in range(1,n+1):
            y=0
            while x:
                y+=x%10
                x//=10
            c[y]+=1
        return c.count(max(c))