class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ba=format(a, '#034b')[2:]
        bb=format(b, '#034b')[2:]
        bc=format(c, '#034b')[2:]
        n=len(ba)
        ans=0
        for i in range(n):
            if bc[i]=='1' and ba[i]!='1' and bb[i]!='1':
                ans+=1
            if bc[i]=='0' and ba[i]!='0':
                ans+=1
            if bc[i]=='0' and bb[i]!='0':
                ans+=1
        return ans

