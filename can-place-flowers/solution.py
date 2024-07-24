class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        i=0
        while i<len(a):
            if (i==0 or a[i-1]==0) and a[i]==0 and (i==len(a)-1 or a[i+1]==0):
                n-=1
                i+=1
            i+=1
        return n<=0