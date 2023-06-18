class Solution:
    def distanceTraveled(self, x: int, y: int) -> int:
        ans=0
        while x>=5:
            x-=5
            if y>0:
                y-=1
                x+=1
            ans+=50
        ans+=x*10
        return ans
            
            
        