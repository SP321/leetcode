class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        a=list(zip(damage,health))
        a.sort(key=lambda x:-x[0]/ ((x[1]+power-1)//power) )
        total=sum(damage)
        ans=0
        for x,y in a:
            ans+=total * ( (y+power-1)//power )
            total-=x
        return ans
