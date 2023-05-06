class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=int(1e9)
        ans=j
        while i<=j:
            hoursum=0
            m=i+(j-i)//2
            for x in piles:
                hoursum+=(x+m-1)//m
            if hoursum>h:
                i=m+1
            else:
                ans=m
                j=m-1
        return ans